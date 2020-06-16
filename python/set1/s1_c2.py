"""
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
"""

def join(s1, s2):
	return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)])

orig = '1c0111001f010100061a024b53535009181c'
mask = '686974207468652062756c6c277320657965'

origBytes = orig.decode('hex')
maskBytes = mask.decode('hex')

print join(origBytes, maskBytes)
print join(origBytes, maskBytes).encode('hex')
