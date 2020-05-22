'''
동시에 번식할 경우, 큰수가 번실을 한다.
생명력 수치가 2인경우
0시간, 1시간 ,2시간, 3시간, 4시간, 5시간,6시간
        비 활 성  /  활 성     / 비 활 성
생명력의 2배가 될때마다 활성상태가 된다.
생명력 1의 경우 2시간에 1칸씩 추가...

입력
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
'''
dx = [-1,0,1,0]     # y축 이동 N
dy = [0,1,0,-1]     # x축 이동 M

N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
k = K//2
cnt = 0
while cnt < k:
    cnt +=1
    for y in range(M):
        for x in range(N):
            if arr[x][y] != 0:
                if arr[x][y] % cnt