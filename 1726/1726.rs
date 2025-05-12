fn main () {
    let n: i64 = {
        let mut buf = String::new();
        std::io::stdin().read_line(&mut buf).expect("input");
        buf.trim().parse().unwrap()
    };
    
    let mut xs: Vec<i64> = Vec::new();
    xs.resize(10_000, 0);
    
    let mut ys: Vec<i64> = Vec::new();
    ys.resize(10_000, 0);

    for _ in 0..n {

        let pair: Vec<i64> = {
            let mut buf = String::new();
            std::io::stdin().read_line(&mut buf).expect("input");
            println!("`{buf}`");
            buf
                .trim()
                .split(" ")
                .flat_map(|s| {s.parse()})
                .collect()
        };

        xs.push(pair[0]);
        ys.push(pair[1]);
    }

    xs.sort();
    ys.sort();

    let mut cumsum_x: Vec<i64> = Vec::with_capacity(n as usize);
    let mut cumsum_y: Vec<i64> = Vec::with_capacity(n as usize);

    cumsum_x[0] = xs[0];
    cumsum_y[1] = ys[0];
    
    for i in 1..n as usize {
        cumsum_x[i] = xs[i] + cumsum_x[i-1];
        cumsum_y[i] = ys[i] + cumsum_y[i-1];
    }

    let sum = {
        let mut sum = 0;
        for i in 1..n as i64 {
            sum += i*xs[i as usize]-cumsum_x[(i-1) as usize];
            sum += i*ys[i as usize]-cumsum_y[(i-1) as usize];
        }
        sum
    };

    println!("{}", sum / (n*(n-1)/2) );

 
}