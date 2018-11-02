import re

morse = {
	'.-':'A',
	'-...':'B',
	'-.-.':'C',
	'-..':'D',
	'.':'E',
	'..-.':'F',
	'--.':'G',
	'....':'H',
	'..':'I',
	'.---':'J',
	'-.-':'K',
	'.-..':'L',
	'--':'M',
	'-.':'N',
	'---':'O',
	'...':'S',
	'-':'T',
	'..-':'U',
	'...-':'V',
	'.--':'W',
	'-..-':'X',
	'-.--':'Y',
	'--..':'Z'
}

with open('morse.in') as f:
	for line in f:
		t = []
		for s in line.strip().split(' '):
			t.append(morse.get(s) if s else ' ')
		print(re.sub(' +', ' ', ''.join(t)))
