#2115. [모의 SW 역량테스트] 벌꿀채취
# a = [16,6,5,3,4,1,6,7,13,36,675]
# a = sorted(a,reverse=True)
# print(a)
def dfs(x,y,n,k):
    global used
    if n == k:
        for i in used:
            if i == 1:

        print(used)
    else:
        used[n] = 1
        (x,y,n+1,k)
        used[n] = 0
        (x, y, n + 1, k)


n,m,c = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]
total = []     # 가장 큰 두자리를 위한것
used = [0]*m
for i in range(n):
    for j in range(n-m+1):
        if sum(rm[i][j:j + m]) == c or sum(rm[i][j:j+m]) >= c:
            dfs(i,j,0,m)
            for x in range(i,n):
                for y in range(j,n-m+1):
                    if sum(rm[x][y:y + m]) == c or sum(rm[x][y:y + m]) >= c:

        re = comp=0
        # c와 같을경우
        if sum(rm[i][j:j+m]) == c:
            for k in rm[i][j:j+m]:
                re +=k**2
            total.append(re)
        elif sum(rm[i][j:j+m]) > c:
            per(rm[i][j:j+m],0,m)

            result = sorted(rm[i][j:j + m],reverse=True)
            for k in result:
                comp += k
                if c > comp:
                    re +=k**2
            total.append(re)
total.sort()
print(total)