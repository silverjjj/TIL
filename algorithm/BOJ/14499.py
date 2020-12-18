
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

def find(x,y,cur):  # cur은 주사위 바닥면

    if cur == "a":
        print(dict["b"])
    elif cur == "b":
        print(dict["a"])
    elif cur == "c":
        print(dict["d"])
    elif cur == "d":
        print(dict["c"])
    elif cur == "e":
        print(dict["f"])
    elif cur == "f":
        print(dict["e"])

    for k in arr:
        x += dx[k]
        y += dy[k]
        print(dict)
        print('이전 바닥면', cur, ' and k', k)
        cur = rotate[cur][k]  # 이동
        print('다음바닥면', cur)
        if mapping[x][y] == 0:
            mapping[x][y] = dict[cur]
        else:
            dict[cur] = mapping[x][y]
        # 여기 윗면 출력력

        if cur == "a":
            print(dict["b"])
        elif cur == "b":
            print(dict["a"])
        elif cur == "c":
            print(dict["d"])
        elif cur == "d":
            print(dict["c"])
        elif cur == "e":
            print(dict["f"])
        elif cur == "f":
            print(dict["e"])

N,M,x,y,K = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
arr = list(map(int,input().split()))
dict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0}
rotate = {'a' : [0,'e','f','c','d'], # 동 서 북 남
            'b' : [0,'e','f','d','c'],
            'c': [0,'e','f','b','a'],
            'd': [0,'e','f','a','b'],
            'e': [0,'d','c','b','a'],
            'f': [0,'c','d','b','a']}

find(x,y,"a")