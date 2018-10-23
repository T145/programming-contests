s = input().strip().replace('1000001', '')
l = [ s[i:i+7] for i in range(0, len(s), 7) ]
s = ''.join([chr(int(c, 2)) for c in l])
print(s)
