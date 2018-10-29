with open('prob4.in') as f:
	l = f.readline()
	while l:
		l = l[:-1].strip().replace('1000001', '')
		s = [ l[i:i+7] for i in range(0, len(l), 7) ]
		l = ''.join([chr(int(c, 2)) for c in s])
		print(l)
		l = f.readline()
