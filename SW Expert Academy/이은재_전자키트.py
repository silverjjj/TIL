def perm(k):
    global minV
    if p[0] == 0:   # 첫출발이 사무실일때만,
        if n == k:  # 모두 방문할경우
            p.append(0)
            sum = j = 0
            while j < len(p)-1:
                sum += rm[p[j]][p[j+1]]
                j += 1
            p.pop()
            if minV > sum:
                minV = sum
        else:
            for i in range(0,n):
                if not visited[i]:
                    p[k] = arr[i]
                    visited[i] = 1
                    perm(k+1)
                    visited[i] = 0
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n # 방문표시를 위한
    arr = [num for num in range(n)]
    minV = 1234567890
    p = [-1] * (n-1) # 결과를 저장하기 위한
    p.insert(0,0)   # 맨처음 0을 삽입 => 출발이 0일때만함수를 돌수있도록하기위해
    perm(0)
    print("#{} {}".format(tc,minV))