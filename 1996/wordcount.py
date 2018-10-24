
import re
from collections import Counter

file = open(r"words.dat", "r", encoding="utf-8-sig")
wordcount = sum(Counter(re.findall(r"[\w']+", file.read())).values())

print("This file contains " + str(wordcount) + " words.")
