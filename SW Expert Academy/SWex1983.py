T = int(input())
for test_case in range(T):
    N,K = list(map(int,input().split()))
    list_sum = []
    count = 0
    for i in range(N):
        count += 1
        score = 0
        Mid , Fin, Ass = map(int,input().split(' '))
        score = Mid * 0.35 + Fin * 0.45 + Ass * 0.2
        list_sum.append(score)

    K_score = list_sum[K-1]  #K의 점수
    list_sum = sorted(list_sum)
    rank = list_sum.index(K_score)    #K점수가 몇번째 index되있는지 추출

    if int(rank*10/N) == 9:
        print(f"#{test_case+1} A+")
    elif int(rank*10/N) == 8:
        print(f"#{test_case+1} A0")
    elif int(rank*10/N) == 7:
        print(f"#{test_case+1} A-")
    elif int(rank*10/N) == 6:
        print(f"#{test_case+1} B+")
    elif int(rank*10/N) == 5:
        print(f"#{test_case+1} B0")
    elif int(rank*10/N) == 4:
        print(f"#{test_case+1} B-")
    elif int(rank*10/N) == 3:
        print(f"#{test_case+1} C+")
    elif int(rank*10/N) == 2:
        print(f"#{test_case+1} C0")
    elif int(rank*10/N) == 1:
        print(f"#{test_case+1} C-")
    elif int(rank*10/N) == 0:
        print(f"#{test_case+1} D0")