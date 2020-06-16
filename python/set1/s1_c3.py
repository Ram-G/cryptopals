"""
Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

"""

def score(string):
	score = 0
	for c in string:
		if c.isalpha():
			score = score + 1
		if c in 'ETAOINSHRDLU' or 'ETAOINSHRDLU'.lower():
			score = score + 1

	score = score + string.count(' ') * 2
	return score

def joinX(s1):
	best, bestMask, bestScore = '', -1, -1
	scores = []
	for i in range(0, 256):
		curr = ''.join([chr(ord(c) ^ i) for c in s1])
		currScore = score(curr)
		scores.append(currScore)
		if currScore >= bestScore:
			best, bestMask, bestScore = curr, i, currScore

	# print scores
	# print scores[bestMask]

	return best, bestMask

def main():
	orig = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	origBytes = orig.decode('hex')

	best, bestMask = joinX(origBytes)
	print best
	print chr(bestMask) + ": " + repr(bestMask)

if __name__ == "__main__":
	main()