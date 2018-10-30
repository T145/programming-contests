with open('buffy.dat') as f:
	idx = 0
	for line in f:
		n, q = list(map(int, line.split()))
		msg = []
		for i in range(n):
			curr = f.readline().split()
			msg.append(curr[q - 1])
			q -= 1
		idx += 1
		print('Message {0} => {1}'.format(idx, ' '.join(msg)))
