def DFS(triangle,depth):
    if depth == 0:
        print(triangle[0][0])
        return triangle[0][0]
    arr = triangle[depth]
    y = len(triangle[depth])
    for j in range(y-1):
        if arr[j] >= arr[j+1]:
            triangle[depth-1][j] += arr[j]
        else:
            triangle[depth - 1][j] += arr[j+1]
    ans = DFS(triangle, depth-1)
    return ans


def solution(triangle):
    n = len(triangle)
    ans = DFS(triangle,n-1)
    # print(ans)
    return ans

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)