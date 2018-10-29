import datetime

with open('dates.dat') as f:
	l = f.readline()
	while l:
		try:
			l = l[:-1]
			d = list(map(int, l.split('/')))
			print(l, "falls on a", datetime.date(d[2], d[0], d[1]).strftime("%A"))
		except ValueError as err:
			print("Invalid date in the input.")
		l = f.readline()
