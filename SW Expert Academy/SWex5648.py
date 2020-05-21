# SWex 5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def f(n,arr):
    sum = 0
    for x in range(4001):
        if sum == result:
            print(x)
            return sum
        dic = {}
        for i in range(n):
            if arr[i][3] != 0:
                arr[i][0] += dx[arr[i][2]]
                arr[i][1] += dy[arr[i][2]]
                if abs(arr[i][0]) <= 2000 and abs(arr[i][1]) <= 2000:
                    # key값이 없으면
                    if (arr[i][0], arr[i][1]) not in dic:
                        # 원소위치가 key, 번호가 value
                        dic[(arr[i][0], arr[i][1])] = i
                    else:
                        # arr[i][3] 새로운애
                        sum += (arr[dic[(arr[i][0], arr[i][1])]][3] + arr[i][3])
                        arr[i][3] = 0
                        arr[dic[(arr[i][0], arr[i][1])]][3] = 0
                    # 이런방식도 있지만 리스트를 사용해서 겹치면 계속해서 집어넣어서 나중에 걸러내는 방식으로도 가능함
    return sum
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = []
    result = 0
    for num in range(n):
        x,y,d,e = map(int,input().split())
        arr.append([2*x,2*y,d,e])
        result += e
    # print(arr)
    ans = f(n,arr)
    print("#{} {}".format(tc,ans))

