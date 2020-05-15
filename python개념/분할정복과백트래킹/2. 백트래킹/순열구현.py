def backtrack(result, visited,k,n):
    if k == n:
        print(result)
        return
    # 사용 가능한 선택지 후보군에 대하여 다음단계로 진행
    for i in range(n):
        if not visited[i]: # 선택되지 않았다면
            visited[i] = 1
            result[k] = i     # result의 idx에 i저장
            backtrack(result, visited, k+1, n)
            visited[i] = 0
n = 5
backtrack([0]*n,[0]*n,0,n)