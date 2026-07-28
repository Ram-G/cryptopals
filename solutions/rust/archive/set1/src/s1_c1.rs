// Convert hex to base64
// The string:
// 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
// 
// Should produce:
// SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

use crate::utils::get_result_message;

const INPUT: &str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
const OUTPUT: &str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";

pub fn main() {
    let raw_bytes = hex::decode(INPUT).unwrap();
    let base64_string = base64::encode(raw_bytes);
    
    let succeeded = base64_string == OUTPUT;
    println!("Challenge 1: {}", get_result_message(succeeded));
    assert!(succeeded);
}