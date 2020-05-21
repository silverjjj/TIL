def combination2(tmp_arr,m,k):
    global sum
    if k == 0:
        # print(food)
        x = food[0]
        y = food[1]
        # print(x,y, rm[x][y],rm[y][x])
        sum += (rm[x][y]+rm[y][x])
        return
    elif m < k:
        return
    else:
        food[k-1] = tmp_arr[m-1]  # 마지막 데이터부터 tr에 넣는다.
        # 1 tr이 꽉찰때까지
        combination2(tmp_arr,m-1,k-1)
        combination2(tmp_arr,m-1,k)

def stop(tr):
    global stan_list
    stan_list.append(tr)
    print(stan_list)

def combination(n,r):
    global sum,minV
    # print(stan_list)
    if r == 0:
        tr2 = list(set(arr)-set(tr))
        if tr2 in stan_list:
            return
        stop(tr)
        sum = 0
        combination2(tr, len(tr),2)
        # print(sum)
        tmp = sum
        sum = 0
        combination2(tr2,len(tr2),2)
        result = abs(tmp-sum)
        if minV > result:
            minV = result
        return
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]  # 마지막 데이터부터 tr에 넣는다.
        # 1 tr이 꽉찰때까지
        combination(n-1,r-1)
        combination(n-1,r)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [list(map(int,input().split())) for _ in range(n)]
    arr = [num for num in range(n)]
    r = n//2
    sum = 0
    minV = 1234567
    sum_list = []
    stan_list = []
    tr = [0]*r # 결과를 담는 배열
    food = [0]*2
    combination(n,r) # n개중 r개를 조합으로 나열
    # print(stan_list)
    print("#{} {}".format(tc,minV))
'''
1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
4
0 7 1 1
7 0 6 2
1 1 0 2
10 1 9 0
6
0 37 26 52 77 20
32 0 15 26 75 16
54 33 0 79 37 90
92 10 66 0 92 3
64 7 89 89 0 21
80 49 94 68 5 0
'''