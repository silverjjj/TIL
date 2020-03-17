# SWex6109. 추억의 2048게임
#

for tc in range(int(input())):
    def f(N,rm):
        ans = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                ans[i][j] = rm[N-j-1][i]
        return ans
    def go(N,rm):
        ans = [[0]*N for _ in range(N)]
        for x in range(N):
            st = []
            for y in range(N):
                if rm[x][y] !=0:
                    st.append(rm[x][y])

            j = N-1
            # print(st)
            while len(st) >=2:
                a = st.pop()
                b = st.pop()
                if a == b:
                    ans[x][j] = a+b
                elif a != b:
                    ans[x][j] = a
                    st.append(b)
                j-=1
            if len(st) == 1:
                # print(st)
                ans[x][j] = st.pop()
        return ans

    n = input().split()
    N= int(n[0])
    S= n[1]
    rm = [list(map(int,input().split())) for _ in range(N)]
    ans = []
    if S =='right':
        ans = go(N,rm)
    elif S=='up':
        rm = f(N,rm)
        ans = go(N,rm)
        for _ in range(3):
            ans = f(N,ans)

    elif S == 'left':
        rm = f(N,rm)
        rm = f(N,rm)
        ans = go(N,rm)
        for _ in range(2):
            ans = f(N,ans)
    elif S == 'down':
        rm = f(N,rm)
        rm = f(N,rm)
        rm = f(N,rm)
        ans = go(N,rm)
        ans = f(N,ans)
    print("#{}".format(tc+1))
    for x in range(N):
        for y in range(N):
            print(ans[x][y], end = " ")
        print()
