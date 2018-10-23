
import re

def encode(s):
	return ''.join(str(ord(c))[::-1] for c in reversed(s))

def decode(s):
	return ''.join(map(chr, map(int, re.findall(r'[01]?\d\d', s[::-1]))))

n = input().strip()
print(encode(n))
print(decode(encode(n)))
