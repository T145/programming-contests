with open('chuck.in') as f:
	l = f.readline()
	while l:
		s = l[:-1].split()
		print(s[0] + ' the woodchuck can chuck', int(s[1]) * 5, 'kilograms of wood.')
		l = f.readline()
