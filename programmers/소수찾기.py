
ans = 0
arr = []
def DFS(numbers,n,r,tr, visited):
    global ans, arr
    if len(tr) >= 1:
        num = int(tr)
        if num > 1 and num not in arr:
            arr.append(num)
            flag = True
            for i in range(2,num):
                if num % i == 0:
                    flag = False
                    break
            if flag:
                ans += 1
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            DFS(numbers, n, r+1, tr + numbers[i], visited)
            visited[i] = 0

def solution(numbers):
    n = len(numbers)
    tr = ""
    visited = [0] * n
    DFS(numbers, n, 0, tr, visited)
    return ans

numbers = "011"
print(solution(numbers))