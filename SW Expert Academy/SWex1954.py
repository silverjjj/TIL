






N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]
matrix[0][0] = 1
    # 오른, 아래, 왼, 위
dr = [0, 1, 0, -1]      # row 열 - 세로
dc = [1, 0, -1, 0]      # columm 행-가로
print(matrix)
currentc =currentr =0
num = 1

while num < N*N:
    for i in range(4):
        nr = currentr + dr[i]q
        nc = currentc + dc[i]         # nc랑 nr은 현재 위치
        while 0 <= nc < N and 0 <= nr < N:
            if matrix[nr][nc] == 0:
                num += 1
                matrix[nr][nc] = num
                print(matrix)
                print(nr, nc)
                currentc = nc
                currentr = nr
                nc = currentc + dc[i]
                nr = currentr + dr[i]
                print(nr, nc)
            else:
                break

print(matrix)