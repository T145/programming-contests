
def search_match(t, f):
	return t.startswith('From veep@whitehouse.gov') and f.startswith('To buddha@whitehouse.gov')

emails = []

with open(r"whmail.log", "r", encoding="utf-8-sig") as f:
	copy = False
	lines = f.readlines()
	for i, line in enumerate(lines):
		if search_match(line, lines[(i + 1) % len(lines)]):
			copy = True
			emails.append(line)
		elif copy and line.startswith('From'):
			copy = False
		elif copy:
			emails.append(line)
		print(copy)

print(emails)
