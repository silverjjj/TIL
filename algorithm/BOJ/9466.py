'''
BOJ9466
N의 최대값은 10만 그러므로 시간복잡도는 O(N)
'''
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [-1] + list(map(int,input().split()))
    visited = [0 for _ in range(N+1)]
    cnt = 0
    for i in range(1,N+1):
        if not visited[i]:
            s = [i]
            st = 0
            dist = { i:st}
            while s:
                cur = s[-1]
                next = arr[cur]
                if visited[cur]:
                    break
                visited[cur] = 1
                if cur == next:
                    cnt += 1
                    break
                if dist.get(next) != None:
                    idx = dist.get(next)
                    cnt += len(s[idx:])
                    break
                s.append(next)
                st += 1
                dist[next] = st
    print(N - cnt)