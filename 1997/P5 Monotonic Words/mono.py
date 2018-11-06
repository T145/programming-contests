def increasing(s):
    return all(x < y for x, y in zip(s, s[1:]))

def decreasing(s):
    return all(x > y for x, y in zip(s, s[1:]))

with open('mono.in') as f:
	for word in f.read().split('\n'):
		if increasing(word) or decreasing(word):
			print(word)
