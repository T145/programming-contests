import re
from collections import Counter

with open('prob2.in') as f:
	l = f.readline()
	while l:
		s = re.sub(r"[^a-z]+", '', l.lower())
		d, c = Counter(s), 0
		for e in d:
			if d[e] / len(l) > 0.15:
				print(e.upper() + ' is a super freq.')
				c += 1
		if (c == 0):
			print('There are no super freqs.')
		l = f.readline()
