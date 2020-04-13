#2115. [모의 SW 역량테스트] 벌꿀채취
# a = [16,6,5,3,4,1,6,7,13,36,675]
# a = sorted(a,reverse=True)
# print(a)
def per(arr,l,m):

    if l == m:

        for i in range(k):
            if used[i] == 0:    # i번 원소가 사용되지 않았다면
                used[i] = 1     # 사용함으로 표시
                p[n] = A[i]
                f(n+1,k)        # n+1 원소결정
                used[i] = 0
    else:
        for i in range(l):
            if used[i] == 0:
                used[i] = 1
        per(arr,l+1,m)

        per(arr, l + 1, m)


n,m,c = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]
total = []     # 가장 큰 두자리를 위한것
for i in range(n):
    for j in range(n-m+1):
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