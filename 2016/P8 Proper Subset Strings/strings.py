for _ in range(int(input())):
	s1, s2 = input(), input()
	subset = s2.startswith(s1) and s2[s2.find(s1)+len(s1)] == ' ' or s2.endswith(s1) and s2[s2.rfind(s1)-1] == ' '
	print('"{}" is{} a proper subset of "{}"'.format(s1, '' if subset else ' not', s2))
