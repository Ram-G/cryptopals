#[macro_use]
extern crate lazy_static;
extern crate hex;
extern crate base64;

mod utils;
mod s1_c1;
mod s1_c2;
mod s1_c3;

fn main() {
    s1_c1::main();
    s1_c2::main();
    s1_c3::main();
}
