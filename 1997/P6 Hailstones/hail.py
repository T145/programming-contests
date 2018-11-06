from itertools import count

def steps(n):
	for i in count():
		if n in {4, 2, 1}:
			return i
		n = n // 2 if n % 2 == 0 else 3 * n + 1

with open('hail.in') as f:
	for n in list(map(int, f.read().split('\n'))):
		print('{} steps were necesary for {}.'.format(steps(n), n))
