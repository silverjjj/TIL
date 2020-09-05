import heapq
def solution(jobs):
    now = res = 0
    n = len(jobs)
    visited = [0] * n
    cnt = 0
    while cnt < n:
        hq = []
        for i in range(n):
            if not visited[i] and jobs[i][0] <= now:
                heapq.heappush(hq, [jobs[i][1],jobs[i][0],i])
        if len(hq) == 0:
            now += 1
            continue
        cnt += 1
        time, start, idx = heapq.heappop(hq)
        now += time
        res += (now-start)
        visited[idx] = 1
    # print(res)
    return res // n

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
