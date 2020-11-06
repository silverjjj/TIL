# 이분탐색으로 푸는문제, 이분탐색은 퀵정렬과 비슷함
import sys
input = sys.stdin.readline
N, M =map(int,input().split())  # N: 심사인원수, M: 친구수
times = [int(input()) for i in range(N)]
left = 0
right = max(times) * M
ans = 0
while left <= right:
    res = 0
    mid = (left + right) // 2
    # print(left, mid, right)
    for time in times:
        res += mid//time
    if res >= M:
        right = mid-1
        ans = mid
    else:
        left = mid + 1
print(ans)