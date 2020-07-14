# 6603_로또
def lotto(st,depth):
    # global result
    if depth == 6:
        for tmp in result:
            print(tmp, end=" ")
        print()
        return
    for i in range(st, n):
        if visited[i] == 0:
            visited[i] = 1
            result[depth] = num[i]
            lotto(i,depth + 1)
            visited[i] = 0
while True:
    number = list(map(int,input().split()))
    if number[0] == 0:
        break
    n = number[0]
    num = number[1:]
    result = [0]*6
    visited = [0]*n
    # print(num)
    lotto(0,0)
    print()