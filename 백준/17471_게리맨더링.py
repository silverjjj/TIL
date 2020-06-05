# 17471_게리맨더링 4시 30분 시작
'''
1~ N개의 구역을 2개의 선거구로 나눈다
2개의 선거구는 적어도 1개 이상의 구역이 있어야함
한 선거구에 있는 구역은 모두 인접해야함
M번 구역에서 N번구역으로 갈때 두 구역은 연결되어야한다. 중간으로 통하는건 XX
입력
N
1 ~ N구역의 인구수
인접한 구역갯수, 인접한 구역번호.....

문제푸는과정
1. 인접 배열 OR 인접리스트 생성
2. 노드 2개를 골라서 1차 인접한 노드를 확인 => 모든 노드가 있다 => 진행
없다 => return
3. 겹치는 노드를 제외한 모든 노드와 자신이 노드의 인구수를 더한다.
4. 겹치는 노드를 순열로 돌려 모든 경우를 따지면서 min값을 구해준다

'''
N = int(input())
population = [0]+list(map(int,input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(1,len(arr)):
        adj[i+1][arr[j]] = 1
        adj[arr[j]][i+1] = 1
        adj[i+1][i+1] = 1


def find(i,j):
    tmp = [0] * (N+1)
    for l in range(1,N+1):
        if adj[i][l] == 1 or adj[j][l] == 1:
            tmp[l] += (adj[i][l] + adj[j][l])
        else:
            return
    tmp2 = []
    for k in range(1,N+1):
        if tmp[k] >= 2:
            if k != i and k != j:
                tmp2.append(k)
    # print(adj[i])
    # print(adj[j])
    # print(tmp)
    arr.append([i,j])
    done.append(tmp2)
arr = []
done = []
for i in range(1,N+1):
    for j in range(i+1,N+1):
        find(i,j)

print(arr)      # 모든 구역을 다 차지한경우
print(done)     # 그때의 겹치는 구역의 idx

def perm(k,do,n,x_sum,y_sum):
    # print(k,x_sum)
    if k > n:
        return
    if k == n:
        print(x_sum,y_sum)
        return
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                x_sum +=population[do[i]]
        perm(k+1, do, n, x_sum ,y_sum)
            x_sum -= population[do[i]]
            y_sum += population[do[i]]
            used[i] = 0
            perm(k+1, do, n, x_sum, y_sum)
            y_sum -= population[do[i]]
    # return
minV = 0
for idx in range(len(done)):
    res = done_sum = x_sum = y_sum = 0
    # 두 개의 노드
    x_node = arr[idx][0]
    y_node = arr[idx][1]
    # x노드와 y노드의 모든 인접한 노드의 합
    for j in range(N):
        if adj[x_node][j] == 1:
            x_sum += population[j]
    for j in range(N):
        if adj[y_node][j] == 1:
            y_sum += population[j]

    if len(done[idx]) > 0:  # 인접한게 있다
        n = len(done[idx]); used = [0] * n
        print("n=>",n)
        for i in done[idx]:
            done_sum += population[i]
            # print(done_sum)
        # print(done_sum)
        x_sum -= done_sum
        y_sum -= done_sum
        print("함수 시작 = > ", x_sum,y_sum)
        print(population[1],population[3])
        perm(0,done[idx],n,x_sum,y_sum)
