
from collections import Counter

s = input().replace(' ', '').lower()
d = Counter(s)
c = 0

for i, e in enumerate(d):
	if d[e] / len(s) * 100 > 15:
		print(e.upper() + ' is a super freq.')
		c += 1

if (c == 0):
	print('There are no super freqs.')
