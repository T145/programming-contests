from collections import Counter

for _ in range(int(input())):
	line = input()
	if line.count(line[0]) == len(line):
		print('{}:solid'.format(line))
	elif all(line[i] < line[i+1] for i in range(len(line)-1)) or all(line[i] > line[i+1] for i in range(len(line)-1)):
		print('{}:ladder'.format(line))
	elif int(line) <= 100:
		print('{}:lower'.format(line))
	elif int(line) >= 99999900:
		print('{}:high'.format(line))
	elif line[:len(line) // 2] == ''.join(reversed(line[len(line) // 2:])):
		print('{}:radar'.format(line))
	elif line[:len(line) // 2] == line[len(line) // 2:]:
		print('{}:repeater'.format(line))
	elif any(str(v[0]) * 7 in line for _, v in enumerate(Counter(line).most_common())):
		print('{}:seven in a row'.format(line))
	elif Counter(line).most_common(1)[0][1] == 7:
		print('{}:seven of a kind'.format(line))
	else:
		print('{}:no pattern'.format(line))
