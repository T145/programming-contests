
"""
It's unknown if we have to consider cases like "Hello,,World!"
and after translating we have "Hello, World!"
"""

import re

n = input().strip().replace('ay', '')
l = re.findall(r"[\w']+", n)
w = ['th', 'kn', 'wh', 'tr', 'sh', 'fl']

for i, s in enumerate(l):
	if s.lower()[-2:] in w:
		p = s[-2:]
		l[i] = p + s[:-2]
	elif s[-1:].lower() is not 'y':
		p = s[-1:]
		l[i] = p + s[:-1]
	else:
		l[i] = s[:-1]

print(l)
