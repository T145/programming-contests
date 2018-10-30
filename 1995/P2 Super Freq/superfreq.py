import re
from collections import Counter

with open('prob2.in') as f:
	for line in f:
		s = re.sub(r"[^a-z]+", '', line.lower())
		d, c = Counter(s), 0
		for e in d:
			if d[e] / len(line) > 0.15:
				print('{0} is a super freq.'.format(e.upper()))
				c += 1
		if (c == 0):
			print('There are no super freqs.')
