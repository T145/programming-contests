
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

r = []

with open(r"morse.in", "r", encoding="utf-8-sig") as f:
	for l in f.readlines():
		t = []
		for s in l[:-1].split(' '):
			t.append(morse.get(s) if s else ' ')
		r.append(re.sub(' +', ' ', ''.join(t)))

print(r)
