
with open(r"buffy.dat", "r", encoding="utf-8-sig") as f:
	lines = f.readlines()

lines = [s.strip() for s in lines]
it = iter(lines)
msgs = []

for s in it:
	d = list(map(int, s.split()))
	N, Q = d[0], d[1]
	msg = []
	for i in range(N):
		curr = next(it).split()
		msg.append(curr[Q - 1])
		Q -= 1
	msgs.append(msg)

for i, msg in enumerate(msgs):
	print("Message ", i, " => " + ' '.join(msg))
