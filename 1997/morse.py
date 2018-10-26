
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
		for s in l.replace('\n', '').split(' '):
			if s:
				t.append(morse.get(s))
			else:
				t.append(' ')
		r.append(re.sub(' +', ' ', ''.join(t)))

print(r)
