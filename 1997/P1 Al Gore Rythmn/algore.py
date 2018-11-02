import datetime

def search_match(t, f):
	return t.startswith('From veep@whitehouse.gov') and f.startswith('To buddha@whitehouse.gov')

def get_date(date):
	prefix = date.strftime('%A, %B ')
	day = date.strftime('%d').lstrip('0')
	postfix = date.strftime(', %Y')
	return '{0}{1}{2}'.format(prefix, day, postfix)

with open('whmail.log') as f:
	for line in f:
		if search_match(line, f.readline()):
			date, subject = datetime.datetime.strptime(f.readline().strip()[5:], "%A, %B %d, %Y"), f.readline()
			subject = 'Re:' + subject[7:]
			limit = date + datetime.timedelta(days=28)
			sent = limit + datetime.timedelta(days=5)
			print('From veep@whitehouse.gov\nTo buddha@whitehouse.gov\nDate {0}\nSubject {1}\nThank you for advising me of your BM. You may not have\nanother BM until {2}'.format(get_date(sent), subject, get_date(limit)))