import re

def encode(s):
	return ''.join(str(ord(c))[::-1] for c in reversed(s.strip()))

def decode(s):
	return ''.join(map(chr, map(int, re.findall(r'[01]?\d\d', s[::-1]))))

with open('prob5.in') as f:
	for i, line in enumerate(f):
		if line.lower().startswith('encode'):
			print('Message {0} (encoded): {1}'.format(i + 1, encode(f.readline())))
		if line.lower().startswith('decode'):
			print('Message {0} (decoded): {1}'.format(i + 1, decode(f.readline())))
