with open('hail.in') as f:
	l = f.readline()
	while l:
		n, a, b, i = int(l[:-1]), [], { 4, 2, 1 }, 0
		while set(a) & b != b:
			if i == 0:
				a.append(n)
			else:
				a.append(a[i-1]/2 if a[i-1] % 2 == 0 else a[i-1]*3+1)
			i += 1
		print(i - len(b), 'steps were necessary for', str(n) + '.')
		l = f.readline()
