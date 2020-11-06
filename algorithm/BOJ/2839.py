num = int(input())
n = num//5
m = 0
if n * 5 == num:
    print(n)
else:
    while True:
        if (num - (5 * n)) % 3 == 0:
            m = (num - (5 * n)) // 3
            print(n+m)
            break
        n -= 1
        if n == -1:
            print(n)
            break
