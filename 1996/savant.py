
import datetime

s = input()
d = list(map(int, s.split('/')))

try:
	date = datetime.date(d[2], d[0], d[1])
	print(s + " falls on a " + date.strftime("%A"))
except ValueError:
	print("Invalid date in the input.")
