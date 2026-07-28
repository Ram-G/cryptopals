// Fixed XOR
// Write a function that takes two equal-length buffers and produces their XOR combination.

// If your function works properly, then when you feed it the string:

// 1c0111001f010100061a024b53535009181c
// ... after hex decoding, and when XOR'd against:

// 686974207468652062756c6c277320657965
// ... should produce:

// 746865206b696420646f6e277420706c6179

use crate::utils::get_result_message;

const INPUT: &str = "1c0111001f010100061a024b53535009181c";
const KEY: &str = "686974207468652062756c6c277320657965";
const OUTPUT: &str = "746865206b696420646f6e277420706c6179";

pub fn bitwise_xor(v1: &[u8], v2: &[u8]) -> Vec<u8> {
    return v1
        .iter()
        .zip(v2.iter())
        .map(|(&x1, &x2)| x1 ^ x2)
        .collect();
}

pub fn main() {
    let raw_bytes = hex::decode(INPUT).unwrap();
    let raw_key = hex::decode(KEY).unwrap();
    
    let result = bitwise_xor(raw_bytes.as_slice(), raw_key.as_slice());

    let succeeded = hex::encode(result) == OUTPUT;
    println!("Challenge 2: {}", get_result_message(succeeded));
    assert!(succeeded);
}