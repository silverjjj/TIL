'''

4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5
'''
X,Y,M = map(int,input().split())
shark = []
# r,c,s,d,z
visited = [[0]*Y for _ in range(X)]
for m in range(M):
    x, y, s, d, z = list(map(int,input().split()))
    shark.append([x,y,s,d,z])
# d=1 이면 x를 s 만큼 빼줌, x-s를 X로 나눠서 몫이 홀수면 d= 2, 짝수면 d=1 나머지를 x로 할당
# d=2 이면 x를 s 만큼 더해줌 x+s를 X로 나눠서 몫이 홀수면 d= 1, 짝수면 d=2 나머지를 x로 할당
# d=3 이면 y를 s만큼 더해줌 y+s를 Y로 나눠서 몫이 홀수면 d = 4, 짝수면 d=3 나머지를 y로 할당
# d=4 이면 y를 s만큼 빼줌 y-s를 Y로 나눠서 몫이 홀수면 d= 3, 짝수면 d=4 나머지를 y로 할당
person = 0
print("=============================")
for x, y, s, d, z in shark:
    visited[x-1][y-1] = z
for row in visited:
    print(row)
while person < Y:
    person += 1
    print(shark)
    rmlist = []
    for j in range(len(shark)):
        print('사람번호= =>',person)
        if shark[j][1] == person:
            rmlist.append(shark[j])
    tmpnum = 1000000
    first_rm = 0
    for rm in rmlist:
        if rm[0] < tmpnum:
            first_rm = rm
            tmpnum = rm[0]
    if tmpnum != 1000000:
        shark.remove(first_rm)
    print(first_rm)
    print("상어가 잡힘")
    print(shark)
    tmp_list = []
    for i in range(len(shark)):
        print("상어 이동 시작!!!!!!")
        x = shark[i][0]; y = shark[i][1]; s = shark[i][2]; d = shark[i][3]; z = shark[i][4]
        tmp_s = s
        print(x,y,s,d,z)
        if d == 1:
            t = -1
            while s >=1:
                # print("d=1일때,,,,,","이동방" )
                s -= 1
                if (x - 1) == 0:
                    t = 1
                    if s >= 1: # 가야할곳이 더 남아있으면
                        d = 2
                elif (x + 1) == X+1:
                    t = -1
                    if s >= 1:
                        d = 1
                x += t

        elif d == 2:
            t = 1
            while s >= 1:
                s -= 1
                if (x - 1) == 0:
                    t = 1
                    if s >= 1:
                        d = 2
                elif (x + 1) == X+1:
                    t = -1
                    if s >= 1:
                        d = 1
                print("d ==>", d)
                x += t

        elif d == 3:
            t = 1
            while s >= 1:
                s -= 1
                if (y - 1) == 0:
                    t = 1
                    if s >= 1:
                        d = 3
                elif (y + 1) == Y+1:
                    t = -1
                    if s >= 1:
                        d = 4
                y += t

        elif d == 4:
            # x, y, s, d, z
            t = -1
            while s >= 1:
                s -= 1
                if (y-1) == 0:
                    t = 1
                    if s >= 1:
                        d = 3
                elif (y+1) == Y+1:
                    t = -1
                    if s >= 1:
                        d = 4
                y += t
                # print("y ==>", y)
        print(shark[i])
        print([x,y,tmp_s,d,z])
        tmp_list.append([x,y,tmp_s,d,z])
    shark = []
    for row in tmp_list:
        shark.append(row[:])
    print("이동 완료")
    print(shark)
    zero = [[0] * Y for _ in range(X)]

    xy = []
    for row in shark:
        tmpx = row[0]-1
        tmpy = row[1]-1
        zero[tmpx][tmpy] += 1
        if zero[tmpx][tmpy] >= 2:
            if (tmpx, tmpy) not in tuple(xy):
                xy.append([tmpx+1, tmpy+1])

    lst = []
    for xa, ya in xy:
        for x, y, s, d, z in shark:
            if xa == x and y == ya:
                lst.append(z)
    if len(lst) != 0:
        ma = max(lst)
        if ma in lst:
            lst.remove(ma)
        for row in shark:
            for l in lst:
                if l == row[-1]:
                    shark.remove(row)

    visited = [[0] * Y for _ in range(X)]
    for x, y, s, d, z in shark:
        if visited[x - 1][y - 1]:
            visited[x - 1][y - 1] +=z

    for row in visited:
        print(row)
# print(shark)