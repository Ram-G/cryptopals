/*
 * Set 1, Challenge 1: Convert hex to base64.
 * Online: https://cryptopals.com/sets/1/challenges/1
 */

#include "../util.h"
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static const char *const START = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
static const char *const EXPECTED = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";

int hex_to_int(char c) {
	if (c >= '0' && c <= '9') {
		return c - '0';
	} else if (c >= 'a' && c <= 'f') {
		return c - 'a' + 10;
	} else {
		return -1;
	}
}

size_t base64_encode(
	const uint8_t *input,
	size_t input_length,
	char *output
) {
	static const char alphabet[] =
		"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		"abcdefghijklmnopqrstuvwxyz"
		"0123456789+/";

	size_t input_index = 0;
	size_t output_index = 0;

	while (input_index < input_length) {
		size_t remaining = input_length - input_index;

		uint8_t a = input[input_index++];
		uint8_t b = remaining > 1 ? input[input_index++] : 0;
		uint8_t c = remaining > 2 ? input[input_index++] : 0;

		uint32_t combined = (a << 16) | (b << 8) | c;

		output[output_index++] = alphabet[(combined >> 18) & 0x3f];
		output[output_index++] = alphabet[(combined >> 12) & 0x3f];
		output[output_index++] = remaining > 1 ? alphabet[(combined >> 6) & 0x3f] : '=';
		output[output_index++] = remaining > 2 ? alphabet[(combined) & 0x3f] : '=';
	}

	output[output_index] = '\0';
	return output_index;
}

static char *solve(void) {
	size_t hex_length = strlen(START);
	size_t byte_length = hex_length / 2;
	size_t base64_length = 4 * ((byte_length + 2) / 3);

	uint8_t bytes[byte_length];

	for (size_t i = 0; i < byte_length; ++i) {
		int high = hex_to_int(START[i * 2]);
		int low = hex_to_int(START[i * 2 + 1]);

		bytes[i] = (uint8_t)(high << 4 | low);
	}

	char *base64_encoded = malloc(base64_length + 1);
	if (base64_encoded == NULL) {
		return NULL;
	}

	base64_encode(bytes, byte_length, base64_encoded);
	return base64_encoded;
}


int main(void) {
	return run_and_verify(solve, EXPECTED);
}
