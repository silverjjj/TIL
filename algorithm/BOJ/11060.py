def solution(N,arr):
    visited = [999999] * N
    visited[0] = 1
    if N == 1:
        return 0
    for i in range(N):
        if arr[i] != 0:
            for j in range(1, arr[i] + 1):
                if i + j >= N:
                    continue
                visited[i + j] = min(visited[i] + 1, visited[i + j])
    if visited[-1] == 999999:
        return -1
    return visited[-1]-1

N = int(input())
arr = list(map(int,input().split()))
print(solution(N,arr))