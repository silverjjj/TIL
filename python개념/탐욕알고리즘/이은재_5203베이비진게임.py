T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    player1=[0]*10
    player2=[0]*10
    flag = 0
    for i in range(0,len(arr),2):
        a = arr[i]
        b = arr[i+1]
        # 플레이어들에게 실시간으로 카드번호 축적하기
        # 1번 - 2번 순서
        player1[a] += 1
        player2[b] += 1

        # 1번 플레이어
        # triplet 찾기
        if player1[a] >= 3:
            flag = 1
        # run 찾기
        if flag == 0:
            for x in range(0,len(player1)-2):
                if player1[x] >= 1 and player1[x+1] >= 1 and player1[x+2] >= 1:
                    flag = 1
                    break
        if flag != 0:
            break

        # 2번 플레이어
        # triplet 찾기
        if player2[b] >= 3:
            flag = 2
        # run 찾기
        if flag == 0:
            for y in range(0,len(player2)-2):
                if player2[y] >= 1 and player2[y+1] >= 1 and player2[y+2] >= 1:
                    flag = 2
                    break
        if flag != 0:
            break

    # print(x,y)
    print("#{} {}".format(tc,flag))