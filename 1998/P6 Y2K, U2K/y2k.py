import datetime

def normalize_year(s):
	year = int(s)
	if year >= 2000:
		year -= 100
	return str(year)

with open('prob6.in') as f:
	for line in f:
		date = datetime.datetime.strptime(line.replace('\n', ''), '%y%j').date()
		print('{0}/{1}'.format(date.strftime('%m/%d'), normalize_year(date.strftime('%Y'))))
