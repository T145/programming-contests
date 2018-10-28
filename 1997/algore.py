import datetime

def search_match(t, f):
	return t.startswith('From veep@whitehouse.gov') and f.startswith('To buddha@whitehouse.gov')

with open('whmail.log') as f:
	l = f.readline()
	while l:
		if search_match(l, f.readline()):
			date, subject = datetime.datetime.strptime(f.readline()[5:-1], "%A, %B %d, %Y"), f.readline()
			subject = 'Re:' + subject[7:]
			limit = date + datetime.timedelta(days=28)
			sent = limit + datetime.timedelta(days=5)
			print('From veep@whitehouse.gov\nTo buddha@whitehouse.gov\nDate', sent, '\nSubject', subject, '\nThank you for advising me of your BM. You may not have\nanother BM until', limit)
		l = f.readline()
