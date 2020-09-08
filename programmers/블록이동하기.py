def expend_board(board):
    n = len(board)
    for i in range(n):
        board[i].insert(0,1)
        board[i].append(1)
    board.insert(0,[1]*(n+2))
    board.append([1]*(n+2))
    return board

def BFS(board):
    n = len(board)
    dx = [-1,1,0,0]; dy = [0,0,1,-1]    #위,아래,오른,왼
    visited = [[0]*n for _ in range(n)]
    visited[1][1] = visited[1][2] = 1
    q = [[1,1,1,2]]
    while q:
        # print(q)
        print("======================================")
        x1,y1,x2,y2 = q.pop(0)  # x1,y1가 고정되는 위치
        for k in range(4):
            print("======================================")
            nx1 = x1+dx[k]
            ny1 = y1+dy[k]
            nx2 = x2 + dx[k]
            ny2 = y2 + dy[k]
            if nx1 == nx2 and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    if (k == 2 or k == 3):
                        if visited[nx2][ny2] == 0:
                            q.append([x1, y1, nx2, ny2])
                            visited[nx2][ny2] = visited[x1][y1] + 1
                        elif visited[nx1][ny1] == 0:
                            visited[nx1][ny1] = visited[x2][y2] + 1
                            q.append([x2, y2, nx1, ny1])
                    elif k == 0:
                        if visited[nx2][ny2] == 0:
                            q.append([x2, y2, nx2, ny2])
                            visited[nx2][ny2] = visited[x2][y2] + 1
                    elif k == 1:
                        if visited[nx1][ny1] == 0:
                            q.append([x1, y1, nx1, ny1])
                            visited[nx1][ny1] = visited[x1][y1] + 1
            elif ny1 == ny2 and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    if (k == 0 or k == 1):
                        if visited[nx2][ny2] == 0:
                            q.append([x1, y1, nx2, ny2])
                            visited[nx2][ny2] = visited[x1][y1] + 1
                        elif visited[nx1][ny1] == 0:
                            visited[nx1][ny1] = visited[x2][y2] + 1
                            q.append([x2, y2, nx1, ny1])
                    elif k == 2:
                        if visited[nx2][ny2] == 0:
                            q.append([x2, y2, nx2, ny2])
                            visited[nx2][ny2] = visited[x2][y2] + 1
                    elif k == 3:
                        if visited[nx1][ny1] == 0:
                            q.append([x1, y1, nx1, ny1])
                            visited[nx1][ny1] = visited[x1][y1] + 1

            for row in visited:
                print(row)

def solution(board):
    board = expend_board(board)
    for row in board:
        print(row)
    BFS(board)

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
solution(board)
