def increasing(s):
    return all(x < y for x, y in zip(s, s[1:]))

def decreasing(s):
    return all(x > y for x, y in zip(s, s[1:]))

result = []

with open('mono.in') as f:
	for line in f:
		line = line[:-1]
		if decreasing(line) or increasing(line):
			result.append(line)

print(result)
