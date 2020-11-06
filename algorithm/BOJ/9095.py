def minus(num):
    global cnt
    if num == 0:
        cnt += 1
        return
    elif num < 0:
        return
    elif num > 0:
        minus(num-1)
        minus(num-2)
        minus(num-3)

T = int(input())
arr = []
for _ in range(T):
    n = int(input())
    arr.append(n)
for num in arr:
    cnt = 0
    minus(num)
    print(cnt)