# SWex4834 ์ซ์์นด๋
for tc in range(1,1+int(input())):
    n = int(input())
    num = list(map(int,input()))

    c = []
    for i in range(n-1):
        c.append(num.count(num[i]))

    if sum(c) == n-1:
        number = max(num)
    else:
        number = num[c.index(max(c))]
    print("#{} {} {}".format(tc,number,max(c)))

