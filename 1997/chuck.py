
with open(r"chuck.in", "r", encoding="utf-8-sig") as f:
	for l in f.readlines():
		s = l[:-1].split(' ')
		print(s[0] + ' the woodchuck can chuck', int(s[1]) * 5, 'kilograms of wood.')
