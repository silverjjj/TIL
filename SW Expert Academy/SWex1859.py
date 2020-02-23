N = int(input())
case = list(map(int,input().split()))
cases = []
a = cnt =0
next = 1
max(case)
for i in range(N):
    print(case[i])
    if case[i] >= next:
        cases.append(case[i])
        next = case[i]
        cnt +=1
    elif case[i] < next:
        a += next*cnt - sum(cases)
        cases.append(case[i])
        print(a, cases)
        next = 1
        cnt = 0

