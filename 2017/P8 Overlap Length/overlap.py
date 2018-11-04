def get_substrs(s):
	substrs = []
	substrs.append(s)
	while s:
		s = s[:-1]
		substrs.append(s)
	return substrs[:-1]

for _ in range(int(input())):
	s1, s2 = input().upper(), input().upper()
	overlap = 0
	for substr in get_substrs(s2):
		if s1.endswith(substr):
			overlap += len(substr)
			break
	print('{0} and {1} have an overlap length of {2}'.format(s1, s2, overlap))
