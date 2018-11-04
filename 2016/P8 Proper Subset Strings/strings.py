for _ in range(int(input())):
	s1, s2 = input(), input()
	n = s2.rfind(s1)
	if s2.startswith(s1) and s2[n+len(s1)] == ' ' or s2.endswith(s1) and s2[n-1] == ' ':
		print('"{0}" is a proper subset of "{1}"'.format(s1, s2))
	else:
		print('"{0}" is not a proper subset of "{1}"'.format(s1, s2))
