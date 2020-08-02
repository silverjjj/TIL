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
    for r in range(1, N + 1):
        adj_tmp[r][:] = adj[r][:]
    if adj_tmp[i][j]:
        adj_tmp[i][j] = 0
        adj_tmp[j][i] = 0
    arr.append([i,j])
    done.append(tmp2)
    adj_list.append([adj_tmp[i][:],adj_tmp[j][:]])

def subset(k,done_sum,x_sum,y_sum,overlap):
    global minV
    if k == n:
        # print("함수bit",bit)
        tmp_res = 0
        for i in range(n):
            if bit[i]:
                tmp_res+=overlap[i]
        # print("tmp_res : ",tmp_res)
        x_sum += tmp_res
        y_sum += (done_sum-tmp_res)
        if minV > abs(x_sum-y_sum):
            minV = abs(x_sum-y_sum)
        # print("minV : ",minV)
    else:
        bit[k] = 0
        subset(k+1, done_sum,x_sum,y_sum,overlap)
        bit[k] = 1
        subset(k + 1, done_sum,x_sum,y_sum,overlap)


N = int(input())
population = [0]+list(map(int,input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(1,len(arr)):
        adj[i+1][arr[j]] = 1
        adj[arr[j]][i+1] = 1
        adj[i+1][i+1] = 1
adj_tmp = [[0]*(N+1) for _ in range(N+1)]

arr = []
done = []
adj_list = []
for i in range(1,N+1):
    for j in range(i+1,N+1):
        find(i,j)
minV = 123456789
for idx in range(len(done)):
    res = done_sum = x_sum = y_sum = 0
    # 두 개의 노드
    x_node = arr[idx][0]
    y_node = arr[idx][1]
    # x노드와 y노드의 모든 인접한 노드의 합
    x_lst = adj_list[idx][0]
    y_lst = adj_list[idx][1]
    for i in range(1, N+1):
        if x_lst[i]:
            x_sum += population[i]
    for j in range(1,N+1):
        if y_lst[j]:
            y_sum += population[j]
    # print("x_node와 y_node는 각각",x_node, y_node)
    # print("x_node의 인접노드는 =>",x_lst)
    # print("y_node 인접노드는 =>", y_lst)
    # print("2개 노드의 모든 인접합은 각각 => ",x_sum,y_sum)
    if len(done[idx]) > 0:  # 인접한게 있다
        n = len(done[idx]); bit = [0] * n
        for i in done[idx]:
            done_sum += population[i]
        # print("done_sum : ",done_sum)
        x_sum -= done_sum
        y_sum -= done_sum
        # print("x_sum,y_sum : ",x_sum,y_sum )
        subset(0,done_sum,x_sum,y_sum,done[idx])
    else:
        if minV > abs(x_sum - y_sum):
            minV = abs(x_sum - y_sum)
if minV == 123456789:
    minV = -1
print(minV)