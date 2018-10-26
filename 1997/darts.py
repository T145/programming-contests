
scores = [ 500, 300, 250, 200, 150, 100, 75, 50, 25, 10 ]

def calculate_score(x,y):
	sx, sy = int(x/50), int(y/50)
	if sx > len(scores) or sy > len(scores):
		return 0
	else:
		return scores[sx if x > y else sy]

with open(r"darts.in", "r", encoding="utf-8-sig") as f:
	it = iter(f)
	for l in it:
		l = l[:-1]
		if not any(c.isdigit() for c in l):
			print('Score Summary for', l)
			print(''.ljust(len(l) + 18).replace(' ', '-'))
			n = next(it)[:-1]
			r = []
			for i in range(5):
				coords = list(map(int, n.split()))
				score = calculate_score(coords[0], coords[1])
				print('Hit ', i + 1, ' = ', score)
				r.append(score)
				if i < 4:
					n = next(it)[:-1]
			print('              ' + ''.ljust(len(l) + 4).replace(' ', '-'))
			print('Score =', sum(r))
