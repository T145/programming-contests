with open('prob4.in') as f:
	for line in f:
		print(''.join([chr(int(c, 2)) for c in (line[i:i+7] for i in range(0, len(line), 7)) if c != "1000001"]))
