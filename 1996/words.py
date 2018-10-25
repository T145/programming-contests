
import re
from collections import Counter

with open(r"buffy.dat", "r", encoding="utf-8-sig") as f:
	c = sum(Counter(re.findall(r"[\w']+", f.read())).values())

print("This file contains " + str(c) + " words.")
