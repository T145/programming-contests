from math import hypot

scores = [500, 300, 250, 200, 150, 100, 75, 50, 25, 10]

with open('darts.in') as f:
	name = f.readline()
	while name:
		total = 0
		print('Score Summary for {}'.format(name.strip()))
		print('-' * 23)
		for i in range(5):
			x, y = map(int, f.readline().split())
			idx = int(hypot(x, y) // 50)
			score = scores[idx] if idx < 10 else 0
			print('   Hit {} = {:>12}'.format(i + 1, score))
			total += score
		print(' ' * 14 + '-' * 9)
		print('   Score = {:>12}'.format(total) + '\n')
		name = f.readline()
