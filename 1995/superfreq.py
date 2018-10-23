
def char_freqency(s):
	d = {}
	for n in s:
		if n in d.keys():
			d[n] += 1
		else:
			d[n] = 1
	return d

s = input().replace(' ', '').lower()
d = char_freqency(s)
c = 0

for i, e in enumerate(d):
	if d[e] / len(s) * 100 > 15:
		print(e.upper() + ' is a super freq.')
		c += 1

if (c == 0):
	print('There are no super freqs.')
