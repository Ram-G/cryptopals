// Single-byte XOR cipher
// The hex encoded string:

// 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
// ... has been XOR'd against a single character. Find the key, decrypt the message.

use std::collections::HashSet;

use crate::s1_c2::bitwise_xor;

const INPUT: &str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";

lazy_static! {
    static ref TEST_CHARACTERS: HashSet<char> =
    ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U']
    .iter().cloned().collect();
}

fn score(text: &str) -> u32 {
    let mut score = 0u32;
    for c in text.chars() {
        if TEST_CHARACTERS.contains(&c.to_ascii_uppercase()) {
            score += 1;
        }
    }
    score += (text.matches(" ").count() * 2) as u32; 
    return score;
}

pub fn main() {
    let raw_bytes = hex::decode(INPUT).unwrap();    
    let num_bytes = raw_bytes.len();

    let mut best_score = 0u32;
    let mut best_string = String::new();
    for key in 0..=255u8 {
        let key_vec: Vec<u8> = 
            std::iter::repeat(key)
            .take(num_bytes)
            .map(|x| x as u8)
            .collect();
        let decrypted_bytes = bitwise_xor(raw_bytes.as_slice(), key_vec.as_slice());
        if let Ok(candidate_text) = String::from_utf8(decrypted_bytes)
        {
            let score = score(&candidate_text);
            // println!("{}, score: {}", candidate_text, score);
            if score > best_score {
                best_score = score;
                best_string = candidate_text;
            }
        }
    }

    println!("Challenge 3: decrypted text: {}, score: {}", best_string, best_score);
}