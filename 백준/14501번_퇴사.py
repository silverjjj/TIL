# 14501_퇴사
def find(k,total):
    global maxV
    if k <= (n+1) and total > maxV:
        maxV = total

    if k > n+1:
        return

    for i in range(k, n+1):
        if not visited[i]:
            visited[i] = 1
            find(i+day[i], total+pay[i])
            visited[i] = 0

n = int(input())
day = [0]
pay = [0]
maxV = 0
for _ in range(n):
    x,y = map(int,input().split())
    day.append(x)
    pay.append(y)
visited = [0]*(n+1)
find(1,0)
print(maxV)
