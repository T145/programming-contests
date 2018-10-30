import re
from collections import Counter

with open('words.dat') as f:
	print("This file contains {0} words.".format(sum(Counter(re.findall(r"[\w']+", f.read())).values())))
