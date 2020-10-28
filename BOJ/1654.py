import sys
input = sys.stdin.readline
K,N = map(int,input().split())
nums = []
for _ in range(K):
    nums.append(int(input()))
left = 1
right = max(nums)
maxV = 0
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for num in nums:
        cnt += (num // mid)
    if N > cnt:
        right = mid - 1
    else:
        left = mid + 1
        if mid > maxV:
            maxV = mid
print(maxV)
