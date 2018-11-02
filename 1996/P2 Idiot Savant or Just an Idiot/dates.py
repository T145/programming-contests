import datetime

with open('dates.dat') as f:
	for line in f:
		try:
			month, day, year = list(map(int, line.split('/')))
			print('{0} falls on a {1}.'.format(line.strip(), datetime.date(year, month, day).strftime("%A")))
		except ValueError:
			print("Invalid date in the input.")
