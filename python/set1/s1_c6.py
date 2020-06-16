import sys

from s1_c3 import joinX, score
from s1_c5 import applyRepeatXOR

"""
Break repeating-key XOR
It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed.
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
"""

def bitwiseXOR(s1, s2):
	return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)])

def hammingDistance(s1, s2):
	if len(s1) != len(s2):
	    return ValueError("aah")

	return sum(bin(ord(c)).count("1") for c in bitwiseXOR(s1, s2))

# Assert correct implementation of hammingDistance
assert hammingDistance("this is a test", "wokka wokka!!!") == 37

filename = '6.txt' if len(sys.argv) == 1 else sys.argv[1]
encoding = 'base64' if len(sys.argv) == 1 else sys.argv[2]

# Read data from file and prepare for use
content = []
with open(filename) as f:
	content = f.readlines()

content = [x.strip('\n') for x in content]
content = ''.join([x.decode(encoding) for x in content])

# Find the Hamming distances for each key size
distances, bestKeySize, smallestDist = [], -1, 10000
for keySize in range(2, 40):
	# Take the first 8 chunks of data and compute the average distance
	parts = [content[i:i+keySize] for i in range(0, keySize*16, keySize)]
	dist_ = [hammingDistance(parts[i], parts[i+1]) / float(keySize) for i in range(0, 16, 2)]
	distAvg = sum(dist_) / float(len(dist_))

	distances.append((distAvg, keySize))
	if distAvg < smallestDist:
		bestKeySize, smallestDist = keySize, distAvg

# Select the best 3 key sizes
distances.sort()
bestKeySizes = [distances[0][1], distances[1][1], distances[2][1]]

bestKey, bestDecoded, bestScore = "", "", -1
scores = []
for bestKeySize in bestKeySizes:
	# Split the data into keySize size chunks
	parts = [content[i:i+bestKeySize] for i in range(0, len(content), bestKeySize)]
	transpose = []
	for i in range(bestKeySize):
		# Transpose the data, grouping bytes of corresponding to the same key position together
		transpose.append([s[i] for s in parts if i < len(s)])

	keyL = []
	# Predict each character of the key
	for i in range(bestKeySize):
		dec, key = joinX(transpose[i])
		keyL.append(chr(key))

	# Decode the data and calculate the score
	currKey = ''.join(keyL)
	decoded = applyRepeatXOR(content, currKey)
	decodedScore = score(decoded)

	# print "\n-------- GUESS --------"
	# print "KEY: " + currKey
	# print decoded

	scores.append(decodedScore)
	if decodedScore > bestScore:
		# Keep track of the key that gives the best score on decoded data
		bestDecoded, bestKey, bestScore = decoded, currKey, decodedScore

print "KEY: " + bestKey + "\n----------------------"
print bestDecoded

# print scores

