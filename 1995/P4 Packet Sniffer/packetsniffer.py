with open('prob4.in') as f:
	for line in f:
		line = line.strip().replace('1000001', '')
		s = [ line[i:i+7] for i in range(0, len(line), 7) ]
		line = ''.join([chr(int(c, 2)) for c in s])
		print(line)
