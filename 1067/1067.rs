struct Directory {
    name: String,
    children: Vec<Directory>,
}


impl Directory {
    fn new(name: &str) -> Directory {
        return Directory { name: name.to_string(), children: vec![] };
    }

    fn add_child(&mut self, dir: Directory) {
        let _ = &self.children.push(dir);
        self.children.sort_by(|a, b| {a.name.cmp(&b.name)});
    }

    fn print_tree(&self, depth: i64, print_name: bool) {
        if print_name {
            println!("{}{}", " ".repeat(depth as usize), &self.name);
        }
        let _ = &self.children.iter().for_each(
            |child| {
                child.print_tree(depth+1, true);
            }
        );
    }
    
    fn add_by_path(&mut self, path: &mut Vec<&str>) {
        if path.len() == 0 {
            return;
        }
        let subdir_name = path.remove(0);
        for child in &mut self.children {
            if child.name == subdir_name {
                child.add_by_path(path);
                return;
            }
        }
        let mut d = Directory::new(subdir_name);
        d.add_by_path(path);
        self.add_child(d);

    }
}


fn main() {
    let mut root = Directory::new("root");

    let n = {
        let mut buf = String::new();
        std::io::stdin().read_line(&mut buf).expect("input");
        buf.trim().parse::<usize>().unwrap()
    };

    for _ in 0..n {
        let mut buf = String::new();
        std::io::stdin().read_line(&mut buf).expect("input");
        
        let mut path: Vec<&str> = buf
            .trim()
            .split("\\")
            .collect();

        root.add_by_path(&mut path);
    }

    root.print_tree(-1, false);
}