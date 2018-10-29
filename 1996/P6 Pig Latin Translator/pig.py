import re

w = ['th', 'kn', 'wh', 'tr', 'sh', 'fl']

with open('pig.dat') as f:
	l = f.readline()
	while l:
		n = l.replace('ay', '')
		l = re.findall(r"[\w']+", n)
		for i, s in enumerate(l):
			if s.lower()[-2:] in w:
				p = s[-2:]
				l[i] = p + s[:-2]
			elif s[-1:].lower() is not 'y':
				p = s[-1:]
				l[i] = p + s[:-1]
			else:
				l[i] = s[:-1]
		print(' '.join(l))
		l = f.readline()
