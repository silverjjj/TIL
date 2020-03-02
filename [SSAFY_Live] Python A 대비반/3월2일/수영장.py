'''
10
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300
0 0 0 0 0 0 0 0 6 2 7 8
'''
def find_dfs(n, s, d, m, m3):  #월,총액
    global minV
    if n > 12:
        if minV > s:  #최저가구하기 위해 기준보다 작으면 기준을 다시설정
            minV = s
    elif minV <=s:
        return

    else:
        find_dfs(n+1, s+(d*table[n]),d,m,m3)   #한달씩 추가
        find_dfs(n+1, s+m, d, m, m3)
        # find_dfs(n+1, s + min(table[n]*d,m), d, m, m3)   일 vs 1달을 비교해서 작은값으로 재귀해도된다.
        find_dfs(n+3, s+m3, d, m, m3)             #세달씩 추가

for tc in range(1,1+int(input())):
    d,m,m3,y = map(int,input().split())
    # 1일, 1달, 3달, 1년
    minV = y        #1년의 비용을 기준으로 설정
    table = [0] + list(map(int,input().split()))
    find_dfs(1, 0, d, m, m3)   # 월, 총액을 시작
    print("#{} {}".format(tc,minV))

'''

'''









