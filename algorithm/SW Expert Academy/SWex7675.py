for _ in range(1,9):
    tc = int(input())
    case = list(map(int,input().split()))
    cnt = 0
    while case[-1] > 0:
        cnt += 1
        case.append(case.pop(0)-cnt)
        if cnt == 5:
            cnt = 0
    case[-1] = 0
    print(f"#{tc}",end = " ")
    for i in case:
        print(i,end = " ")
    print()


