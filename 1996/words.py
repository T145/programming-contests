import re
from collections import Counter

with open('words.dat') as f:
	print("This file contains", sum(Counter(re.findall(r"[\w']+", f.read())).values()), "words.")
