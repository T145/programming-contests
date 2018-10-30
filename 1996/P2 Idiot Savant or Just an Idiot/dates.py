import datetime

with open('dates.dat') as f:
	for line in f:
		try:
			d = list(map(int, line.split('/')))
			print('{0} falls on a {1}.'.format(line[:-1], datetime.date(d[2], d[0], d[1]).strftime("%A")))
		except ValueError as err:
			print("Invalid date in the input.")
