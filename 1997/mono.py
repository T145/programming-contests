
def increasing(L):
    return all(x < y for x, y in zip(L, L[1:]))

def decreasing(L):
    return all(x > y for x, y in zip(L, L[1:]))

with open(r"mono.in", "r", encoding="utf-8-sig") as f:
	lines = f.readlines()

result = []

for s in lines:
	s = s.replace("\n", '')
	if decreasing(s) or increasing(s):
		result.insert(0, s)

print(result)
