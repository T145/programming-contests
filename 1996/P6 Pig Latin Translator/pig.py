import re

w = ['th', 'kn', 'wh', 'tr', 'sh', 'fl']

with open('pig.dat') as f:
	for line in f:
		line = re.findall(r"[\w']+", line.replace('ay', ''))
		for i, s in enumerate(line):
			if s.lower()[-2:] in w:
				line[i] = s[-2:] + s[:-2]
			elif s[-1:].lower() is not 'y':
				line[i] = s[-1:] + s[:-1]
			else:
				line[i] = s[:-1]
		print(' '.join(line))
