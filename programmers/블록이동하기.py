dx = [-1,1,0,0]; dy = [0,0,1,-1]    #위,아래,오른,왼
def BFS(x1,y1,x2,y2,n,visited,board): # move_x, move_y, stay_x, stay_y
    print("=======================")
    # if m == 1:
    #     dx = [-1, 1, 0, 0]; dy = [0, 0, 1, -1]
    # elif m == 2:
    #     dx = [0,0,-1,1]; dy = [1,-1,0,0]
    q = [[x1,y1,x2,y2],[x2,y2,x1,y1]]

    while q:
        print('q==>',q)
        x1, y1, x2, y2 = q.pop(0)
        print("x1,y1,x2,y2 ==> ",x1,y1,x2,y2)
        if (y1 - y2) != 0:
            print('가로')
            dx = [-1, 1, 0, 0]; dy = [0, 0, 1, -1]
        else:
            print('세로')
            dx = [0, 0, -1, 1]; dy = [1, -1, 0, 0]

        for k in range(4):
            nx = x2 + dx[k]
            ny = y2 + dy[k]
            # (visited[x2][y2] + 1 <= visited[nx][ny]) or
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] and ((visited[x2][y2] >  visited[nx][ny]) or not visited[nx][ny]):
                # print("k ==>",k)
                if k == 0 or k == 1:
                    nmx = x1+dx[k]; nmy = y1+dy[k]
                    if 0 <= nmx < n and 0 <= nmy < n and not board[nmx][nmy]:
                        pass
                    else:
                        continue
                visited[nx][ny] = visited[x2][x2] + 1
                # print([x2,y2,nx,ny])
                q.append([x2,y2,nx,ny])
                q.append([nx, ny,x2, y2])
        for row in visited:
            print(row)
def solution(board):
    answer = 0
    n = len(board)
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = visited[0][1] = 1

    BFS(0, 0, 0, 1, n, visited, board)
    # q = [[0,0,0,1]]
    # while q:
    #     x1,y1,x2,y2 = q.pop(0)
    #     print(x1,y1,x2,y2)
    #     # 가로 세로 판단
    #     if (y1 - y2) != 0:
    #         BFS(x1,y1,x2,y2,n,visited,board,1)
    #         BFS(x2,y2,x1,y1,n,visited,board,1)
    #         # 가로
    #     else:
    #         # 세로
    #         BFS(x1, y1, x2, y2, n, visited, board,2)
    #         BFS(x2, y2, x1, y1, n, visited, board,2)
    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
solution(board)

















# def expend_board(board):
#     n = len(board)
#     for i in range(n):
#         board[i].insert(0,1)
#         board[i].append(1)
#     board.insert(0,[1]*(n+2))
#     board.append([1]*(n+2))
#     return board
#
# def BFS(board):
#     n = len(board)
#     dx = [-1,1,0,0]; dy = [0,0,1,-1]    #위,아래,오른,왼
#     visited = [[0]*n for _ in range(n)]
#     visited[1][1] = visited[1][2] = 1
#     q = [[1,1,1,2]]
#     while q:
#         # print(q)
#         print("======================================")
#         x1,y1,x2,y2 = q.pop(0)  # x1,y1가 고정되는 위치
#         for k in range(4):
#             print("======================================")
#             nx1 = x1+dx[k]
#             ny1 = y1+dy[k]
#             nx2 = x2 + dx[k]
#             ny2 = y2 + dy[k]
#             if nx1 == nx2 and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
#                     if (k == 2 or k == 3):
#                         if visited[nx2][ny2] == 0:
#                             q.append([x1, y1, nx2, ny2])
#                             visited[nx2][ny2] = visited[x1][y1] + 1
#                         elif visited[nx1][ny1] == 0:
#                             visited[nx1][ny1] = visited[x2][y2] + 1
#                             q.append([x2, y2, nx1, ny1])
#                     elif k == 0:
#                         if visited[nx2][ny2] == 0:
#                             q.append([x2, y2, nx2, ny2])
#                             visited[nx2][ny2] = visited[x2][y2] + 1
#                     elif k == 1:
#                         if visited[nx1][ny1] == 0:
#                             q.append([x1, y1, nx1, ny1])
#                             visited[nx1][ny1] = visited[x1][y1] + 1
#             elif ny1 == ny2 and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
#                     if (k == 0 or k == 1):
#                         if visited[nx2][ny2] == 0:
#                             q.append([x1, y1, nx2, ny2])
#                             visited[nx2][ny2] = visited[x1][y1] + 1
#                         elif visited[nx1][ny1] == 0:
#                             visited[nx1][ny1] = visited[x2][y2] + 1
#                             q.append([x2, y2, nx1, ny1])
#                     elif k == 2:
#                         if visited[nx2][ny2] == 0:
#                             q.append([x2, y2, nx2, ny2])
#                             visited[nx2][ny2] = visited[x2][y2] + 1
#                     elif k == 3:
#                         if visited[nx1][ny1] == 0:
#                             q.append([x1, y1, nx1, ny1])
#                             visited[nx1][ny1] = visited[x1][y1] + 1
#
#             for row in visited:
#                 print(row)
#
# def solution(board):
#     board = expend_board(board)
#     for row in board:
#         print(row)
#     BFS(board)
#
# board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# solution(board)
