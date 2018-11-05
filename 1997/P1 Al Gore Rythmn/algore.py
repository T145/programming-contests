from datetime import datetime, timedelta
import re

BM_EMAIL_RE = re.compile(
    r'^From (?P<From>veep@whitehouse.gov)$\s+'
    r'^To (?P<To>buddha@whitehouse.gov)$\s+'
    r'^Date (?P<Date>.*)$\s+'
    r'^Subject (?P<Subject>.*)$\s+',
    re.MULTILINE
)

REPLY_TEMPLATE = """From buddha@whitehouse.gov
To veep@whitehouse.gov
Date {reply_date}
Subject Re: {subject}

Thank you for advising me of your BM. You may not have
another BM until {limit_date}."""

def format_date(date):
    return re.sub('0([0-9],)', r'\1', date.strftime('%A, %B %d, %Y'))

with open('whmail.log') as f:
	for email in BM_EMAIL_RE.finditer(f.read()):
		date = datetime.strptime(email.group('Date'), '%A, %B %d, %Y')
		print(REPLY_TEMPLATE.format(
			subject=email.group('Subject'),
			reply_date=format_date(date + timedelta(days=33)),
			limit_date=format_date(date + timedelta(days=28)),
		))
