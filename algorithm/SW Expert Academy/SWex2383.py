# SWex2383. [모의 SW 역량테스트] 점심 식사시간


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [list(map(int,input().split())) for _ in range(n)]
    person = []
    stair = []
    num = 0
    p_cnt=0
    for i in range(n):
        for j in range(n):
            if rm[i][j] == 1:
                p_cnt+=1
                person.append([i,j])
            elif rm[i][j] != 0:
                stair.append([i,j])
    A_value = rm[stair[0][0]][stair[0][1]]
    B_value = rm[stair[1][0]][stair[1][1]]

    A_st = []
    B_st = []
    i = 0
    # print(stair)
    for num in stair:
        # d = rm[num[0]][num[1]]
        for p in person:
            result = abs(num[0] - p[0]) + abs(num[1] - p[1])
            if i == 0:
                A_st.append([result,p])
            else:
                B_st.append([result,p])
        i+=1
    A_st.sort()
    B_st.sort()

    for i in range(p_cnt):
        if A_st[i][:] == B_st[i][:]:
            A_st[i][0] += A_value
            B_st[i][0] += B_value
            if A_st[i][0] > B_st[i][0]:
                A_st[i][0] -= A_value
                B_st[i][0] -= B_value
                A_st.pop(i)
                break
            else:
                A_st[i][0] -= A_value
                B_st[i][0] -= B_value
                B_st.pop(i)
                break

    done = []
    time_A = []
    time_B = []
    cnt = 0
    # print(p_cnt)
    while len(done) != p_cnt or len(time_A) != 0 or len(time_B) != 0:
        # 시간 추가해주는것
        if len(time_A) != 0:
            for i in range(len(time_A)):
                time_A[i] +=1
        if len(time_B) != 0:
            for i in range(len(time_B)):
                time_B[i] += 1
        # 계단을 다 내려가면 pop해줌
        if len(time_A) != 0:
            k=0
            tmp_cnt= 0
            for k in range(len(time_A)):
                if time_A[k] == A_value:
                    tmp_cnt+=1
                k+=1
            for _ in range(tmp_cnt):
                time_A.pop(0)

        if len(time_B) != 0:
            k=0
            tmp_cnt= 0
            for k in range(len(time_B)):
                if time_B[k] == B_value:
                    tmp_cnt+=1
                k+=1
            for _ in range(tmp_cnt):
                time_B.pop(0)

        # 여기서 시간리스트의 내부값이 3or5일때 pop
        cnt +=1
        if len(done) != p_cnt:
            for i,j in A_st:
                if i <= cnt and j[:] not in done:
                    if len(time_A) < 3:
                        done.append(j[:])
                        time_A.append(0)

            for x,y in B_st:
                if x <= cnt and y[:] not in done:
                    if len(time_B) < 3:
                        done.append(y[:])
                        time_B.append(0)

    print("#{} {}".format(tc,cnt+1))