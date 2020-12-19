N = int(input())
chars = [str(input()) for _ in range(N)]
dict = {}
for char in chars:
    for i in range(len(char)):
        cnt = "1"
        for _ in range(len(char)-1-i):
            cnt += "0"
        if dict.get(char[i]) == None:
            dict[char[i]] = int(cnt)
        else:
            dict[char[i]] += int(cnt)
s_dict = sorted(dict.values(), reverse=True)
add, res = 9, 0
for number in s_dict:
    res += (number * add)
    add -= 1
print(res)