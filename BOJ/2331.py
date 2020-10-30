N, cnt = map(int,input().split())
arr = [N]
while True:
    num = arr[-1]
    res = 0
    for i in str(num):
        res += int(i) ** cnt
    if res not in arr:
        arr.append(res)
    else:
        last = arr.index(res)
        break
print(len(arr[:last]))