def comp_club(s, is_vowel):
	s = list(s)
	if is_vowel:
		locs = [i for i, c in enumerate(s) if c in 'AEIOU']
	else:
		locs = [i for i, c in enumerate(s) if c not in 'AEIOU']
	for l, r in zip(locs[:int(len(locs)/2)], reversed(locs)):
		s[l], s[r] = s[r], s[l]
	return ''.join(s)

line = input()
while line != 'LAST':
	print('{}:{}'.format(line, comp_club(comp_club(line, False), True)))
	line = input()
