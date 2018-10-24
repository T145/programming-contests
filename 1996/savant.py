
import datetime

s = input().strip()
d = s.split('/')
d = list(map(int, d))

try:
	date = datetime.date(d[2], d[0], d[1])
	print(s + " falls on a " + date.strftime("%A"))
except ValueError:
	print("Invalid date in the input.")
