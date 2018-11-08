with open('prob1.in') as f:
	for n in f.read().split('\n'):
		a, b = map(int, n.split())
		pa, pb, r = a, b, []
		while a > 0:
			if a & 1:
				r.append(str(b))
			a >>= 1
			b <<= 1
		print('{} x {} = {} = {}'.format(pa, pb, ' + '.join(r), pa * pb))
