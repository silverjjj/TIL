def find_dfs(mon,pay):  #월,총액
    global standard
    if mon == 12:
        if pay < standard:  #최저가구하기 위해 기준보다 작으면 기준을 다시설정
            standard = pay
        return
    elif mon > 12:
        return

    find_dfs(mon+1, pay+(d*day[mon]))   #한달씩 추가
    find_dfs(mon+1, pay+m)
    find_dfs(mon+3, pay+m3)             #세달씩 추가

for tc in range(1,1+int(input())):
    d,m,m3,y = map(int,input().split())
    # 1일, 1달, 3달, 1년
    standard = y        #1년의 비용을 기준으로 설정
    day = list(map(int,input().split()))
    find_dfs(0,0)   # 월, 총액을 시작
    print("#{} {}".format(tc,standard))










