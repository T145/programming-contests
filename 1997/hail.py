
with open(r"hail.in", "r", encoding="utf-8-sig") as f:
	for l in f:
		n = int(l[:-1])
		a = []
		b = { 4, 2, 1 }
		i = 0
		while set(a) & b != b:
			if i == 0:
				a.append(n)
			else:
				a.append(a[i-1]/2 if a[i-1] % 2 == 0 else a[i-1]*3+1)
			i += 1
		print(i - len(b), 'steps were necessary for', str(n) + '.')
