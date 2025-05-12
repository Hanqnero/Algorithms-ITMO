#[inline]
fn read_int() -> i64 {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).expect("input");

    buf.trim().parse().unwrap()
}

fn main() {
    let n = read_int();
    let mut stack: Vec<i64> = vec![];
    let mut stack_top: i64 = 0;
    for _ in 0..n {
        let x = read_int();

        if x > stack_top {
            for i in (stack_top+1)..x {
                stack.push(i);
            }
            stack_top = x;

            continue;
        }

        if stack.pop().unwrap() != x {
            println!{"Cheater"};
            return;
        }

    }
    println!{"Not a proof"};
}
