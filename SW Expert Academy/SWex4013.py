T= int(input())
for tc in range(1,T+1):
    k = int(input())
    arr = [list(map(int,input().split())) for _ in range(4)]
    # for row in arr:
    #     print(row)
    for _ in range(k):
        n, m = map(int, input().split())
        # print(n,m)
        info = []
        total = []
        visited = [0]*4
        info.append([n-1,m])
        total.append([n-1,m])
        while info:
            # print(info)
            x,y = info.pop()
            # print(x,y)
            visited[x] = 1
            if 0<=x+1<4 and visited[x+1] == 0:    # 오른쪽
                if arr[x][2] != arr[x+1][6]:
                    info.append([x+1,-y])
                    total.append([x + 1, -y])
                    visited[x+1] = 1
            if 0<=x-1<4 and visited[x-1] == 0:   # 왼쪽
                if arr[x][6] != arr[x-1][2]:
                    info.append([x - 1, -y])
                    total.append([x-1,-y])
                    visited[x-1] = 1
        # print(visited, total)
        for i in range(len(total)):
            if total[i][1] == 1:
                num = total[i][0]
                tmp = arr[num].pop(7)
                arr[num].insert(0,tmp)
            else:
                num = total[i][0]
                tmp = arr[num].pop(0)
                arr[num].append(tmp)
    sum = 0
    for i in range(4):
        if arr[i][0] == 1:
            sum += arr[i][0]*(2**i)
    print("#{} {}".format(tc,sum))

'''
10
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1
'''