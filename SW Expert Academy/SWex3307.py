def find(n,num):
    global s
    s.append(num[0])
    for i in range(1,n):
        if num[i] > s[-1]:
            s.append(num[i])
        elif num[i] < s[-1]:
            if
            s.pop()
            s.append(num[i])

N = int(input())
case = map(int, input().split())
s = []
find(N,case)