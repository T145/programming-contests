with open('prob6.in') as f:
	l = f.readline()
	while l:
		it = iter(l)
		for c in it:
			b = ''
			if c == '(':
				n = next(it)
				if n.isalnum():
					b += n
			print(b)
		l = f.readline()
