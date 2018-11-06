import datetime

with open('prob6.in') as f:
	for n in f.read().split('\n'):
		date = datetime.datetime.strptime(n, '%y%j').date()
		print('{}/{}'.format(date.strftime('%m/%d'), date.year if date.year < 2000 else date.year - 100))
