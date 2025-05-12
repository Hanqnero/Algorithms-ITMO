use std::io::{Read, Write};

#[inline]
fn read_string() -> String {
    let mut buf = String::new();
    std::io::stdin().read_to_string(&mut buf).expect("input");
    buf.trim().to_string()
}

fn main() {
    let mut capitalize = true;

    let input: String = read_string().to_lowercase();

    for char in input.chars() {
        let out = {
            if capitalize {
                if char.is_alphabetic() {
                    capitalize = false;
                }
                char.to_uppercase().to_string()
            } else {
                if char == '.' || char == '?' || char == '!' {
                    capitalize = true;
                }
                char.to_string()
            }
        };
        print!("{out}");

    }

    std::io::stdout().flush().unwrap();
}
