chars = input()
chars = chars.upper()
dict = {}
for char in chars:
    if char in dict.keys():
        dict[char] += 1
    else:
        dict[char] = 1
maxV = max(dict.values())
num = 0
res = None
for ch, val in dict.items():
    if val == maxV:
        num += 1
        res = ch
if num == 1:
    print(res)
else:
    print("?")