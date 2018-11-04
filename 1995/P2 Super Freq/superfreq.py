from collections import Counter

with open('prob2.in') as f:
	for line in f:
		counts = Counter(c for c in line.upper() if 'A' <= c <= 'Z')
		super_freqs = [c for c, n in counts.items() if n / len(line) > 0.15]
		if not super_freqs:
			print('There are no super freqs.')
		else:
			for c in super_freqs:
				print('{0} is a super freq.'.format(c))
