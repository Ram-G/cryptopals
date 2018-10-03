from s1_c3 import score

"""
Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

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

	if bestScore > 60:
		return best, bestMask
	else:
		return None, None

content = []
with open('4.txt') as f:
	content = f.readlines()

content = [x.strip('\n') for x in content]

for line in content:
	line = line.decode('hex')
	best, bestMask = joinX(line)
	if best is not None and bestMask is not None:
		print best
		print chr(bestMask) + ": " + repr(bestMask)