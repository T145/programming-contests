with open('prob1.in') as f:
	for line in f:
		a, b = list(map(int, line.split()))
		la, lb = [], []
		la.append(a)
		lb.append(b)
		while a != 1:
			a //= 2
			b *= 2
			la.append(a)
			lb.append(b)
		print(la)
		print(lb)
