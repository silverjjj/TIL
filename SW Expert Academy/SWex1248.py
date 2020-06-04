# SWex
'''
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13
'''
T= int(input())
for tc in range(1,T+1):
    V,E,a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    dict = [[] for i in range(V+1)]
    # print(dict)
    for i in range(E):
        p,c = arr[i*2], arr[i*2+1]
        dict[p].append(c)
    num = [a,b]
    done = []
    for i in range(2):
        # print(num[i])
        tmp = []
        tmp_list = []
        tmp.append(num[i])
        while tmp:
            a = tmp.pop()
            for i in range(len(dict)):
                for j in range(len(dict[i])):
                    if dict[i][j] == a:
                        tmp.append(i)
                        tmp_list.append(i)
        done.append(tmp_list)
    number = 0
    for i in done[0]:
        for j in done[1]:
            if i == j:
                number = i
                break
        if number != 0:
            break
    q = []
    q.append(number)
    cnt = 1
    while q:
        idx = q.pop(0)
        for i in range(len(dict[idx])):
            cnt +=1
            q.append(dict[idx][i])
    print("#{} {} {}".format(tc, number,cnt))