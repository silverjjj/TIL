room = [[0]*300 for _ in range(300)]
num = 1
for i in range(1,len(room)):
    for j in range(i):
        room[i-j][j+1] = num
        num +=1
# for row in room:
#     print(row)
T = int(input())
for tc in range(1,T+1):
    p, q = map(int, input().split())
    x=y=0
    for i in range(1,len(room)):
        for j in range(1,len(room)):
            if p ==room[i][j]:
                x+=i
                y+=j
            if q ==room[i][j]:
                x+=i
                y+=j
    print("#{} {}".format(tc,room[x][y]))