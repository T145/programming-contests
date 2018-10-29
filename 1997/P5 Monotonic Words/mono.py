def increasing(s):
    return all(x < y for x, y in zip(s, s[1:]))

def decreasing(s):
    return all(x > y for x, y in zip(s, s[1:]))

result = []

with open('mono.in') as f:
	l = f.readline()
	while l:
		l = l[:-1]
		if decreasing(l) or increasing(l):
			result.append(l)
		l = f.readline()

print(result)
