def BFS(x1,y1,x2,y2,n,board): # move_x, move_y, stay_x, stay_y
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = visited[0][1] = 1
    print("=======================")
    q = [[x1,y1,x2,y2],[x2,y2,x1,y1]]
    while q:
        print("===============================")
        print('q==>',q)
        a,b,c,d= q.pop(0)   # move_x, move_y, stay_x, stay_y
        for i in range(2):
            if i == 0:
                x1 = a; y1 = b; x2 = c; y2 = d
            elif i == 1:
                x2 = a; y2 = b; x1 = c; y1 = d

            print("x1,y1,x2,y2 ==> ",x1,y1,x2,y2)
            if abs(y1 - y2) == 1:
                print('가로')
                dx = [-1, 1, 0, 0]; dy = [0, 0, 1, -1]
            else:
                print('세로')
                dx = [0, 0, -1, 1]; dy = [1, -1, 0, 0]
            for k in range(4):
                nx = x2 + dx[k]
                ny = y2 + dy[k]
                # (visited[x2][y2] + 1 <= visited[nx][ny]) or
                if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] and ((visited[x2][y2] +1 <= visited[nx][ny]) or not visited[nx][ny]):
                    # print("k ==>",k)
                    # 이동 여부를 판단
                    print(visited[x2][y2] +1 ,visited[nx][ny],[nx,ny])
                    if k == 0 or k == 1:
                        nmx = x1+dx[k]; nmy = y1+dy[k]
                        if 0 <= nmx < n and 0 <= nmy < n and not board[nmx][nmy]:
                            pass
                        else:
                            continue
                    visited[nx][ny] = visited[x2][y2] + 1
                    q.append([x2,y2,nx,ny])
        for row in visited:
            print(row)
    return (visited[n-1][n-1] -1)

def solution(board):
    # answer = 0
    n = len(board)
    res = BFS(0, 0, 0, 1, n, board)
    print(res)
    return res

board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
solution(board)

'''
[
[0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 0, 0, 1], 
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 1, 1], 
[0, 0, 1, 0, 0, 0, 0]
]
'''