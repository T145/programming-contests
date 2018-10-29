import re

def encode(s):
	return ''.join(str(ord(c))[::-1] for c in reversed(s.replace('\n', '')))

def decode(s):
	return ''.join(map(chr, map(int, re.findall(r'[01]?\d\d', s[::-1]))))

with open('prob5.in') as f:
	i, l = 0, f.readline()
	while l:
		i += 1
		l = l[:-1]
		if l.lower() == 'encode':
			print('Message', i, '(encoded):', encode(f.readline()))
		if l.lower() == 'decode':
			print('Message', i, '(decoded):', decode(f.readline()))
		l = f.readline()
