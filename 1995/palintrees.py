
def get_components(s):
    pairs = []
    for i, c in enumerate(s):
        if c == "(":
            pairs.append([i,])
        elif c == ")":
            for p in reversed(pairs):
                if len(p) < 2:
                    p.append(i)
                    break
    comps = []
    for p in pairs:
        comps.append(s[p[0]+1:p[1]])
    return [x for x in comps if len(x) > 0]

def char_count(s):
	return len([c for c in s if c not in "()"])

l = get_components(input().strip().replace('()', ''))
print(l)

for i, v in enumerate(l):
	cc = char_count(v)
	nxt = l[(i + 1) % len(l)]
	print(nxt)
