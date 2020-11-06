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
            nums = [i]
            used = [0 for _ in range(N+1)]
            used[i] = 1
            while s:
                cur = s.pop()
                if visited[cur]:
                    continue
                visited[cur] = 1
                next = arr[cur]
                # 백트래킹
                if used[next]:
                    st = nums.index(next)
                    cnt += len(nums[st:])
                    break
                s.append(next)
                used[next] = 1
                nums.append(next)
    print(N - cnt)
'''

7
3 1 3 7 3 4 6

13
7 6 3 4 7 5 7 5 10 11 12 9 9

1
5
2 5 4 5 2


7
6
2 3 4 5 6 2
5
2 5 4 5 2
6
1 3 4 3 2 6
13
2 4 5 2 4 1 8 9 10 11 9 10 10
10
2 5 7 1 6 8 8 3 5 10
10
2 7 10 5 3 3 9 10 6 3
6
2 1 1 2 6 3
'''