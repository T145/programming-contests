with open('buffy.dat') as f:
	l = f.readline()
	while l:
		n, q = list(map(int, l.split()))
		idx, msg = 0, []
		for i in range(n):
			curr = f.readline().split()
			msg.append(curr[q-1])
			q -= 1
		idx += 1
		print("Message", idx, "=>", ' '.join(msg))
		l = f.readline()
