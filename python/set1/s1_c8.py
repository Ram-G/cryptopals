"""
Detect AES in ECB mode
In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
"""

from Crypto.Cipher import AES
from collections import Counter

content = []
with open('8.txt') as f:
	content = f.readlines()

content = [x.strip('\n').decode('hex') for x in content]
dup = []

for line in content:
	c = Counter(line)
	vals = c.values()
	dup.append(len(vals))
