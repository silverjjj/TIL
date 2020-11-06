scode = {211:0, 221:1, 122:2,
         411:3, 132:4, 231:5,
         114:6, 312:7, 213:9, 112:9}

hcode = {
    '0':'0000','1':'0001','2':'0010','3':'0011',
    '4':'0100','5':'0101','6':'0110','7':'0111',
    '8':'1000','9':'1001','A':'1010','B':'1011',
    'C':'1100','D':'1101','E':'1110','F':'1111'}

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    tin = [input() for _ in range(N)]

    # input(16진수)을 2진수로 변환
    mat = ['']*N
    for i in range(N):
        for j in range(M):
            mat[i] += hcode[tin[i][j]]
    ans = 0
    # i : 세로, j : 가로
    for i in range(1,len(mat)-6):
        j = M * 4 - 1
        while j > 56:   # 최소 암호코드 길이 7 * 8
            if mat[i][j] == '1' and mat[i-1][j] =='0':
                c=[0]*8
                for k in range(7,-1,-1):    # 2진수를 암호코드로 변환하기 위해
                    x = y = z = 0
                    while mat[i][j] == '1': z += 1; j -= 1   # 젤 오른쪽 1을 세기
                    while mat[i][j] == '0': y += 1; j -= 1
                    while mat[i][j] == '1': x += 1; j -= 1
                    while mat[i][j] == '0' and k: j -= 1    #0 이동만
                    d = min(x,y,z)
                    c[k] = scode[x//d*100+y//d*10+z//d]
                t = (c[0]+c[2]+c[4]+c[6])*3 + c[1]+c[3]+c[5]+c[7]
                if t % 10 == 0:
                    ans += sum(c)
            j-=1    # 1를 찾으려고 오른 -> 왼쪽 가기위해
    print("#{} {}".format(tc,ans))




