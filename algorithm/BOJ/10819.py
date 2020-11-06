from itertools import permutations

N = int(input())
arr = permutations(list(map(int,input().split(' '))))
maxV = 0
for nums in arr:
    res = 0
    for j in range(N-1):
        res += abs(nums[j] - nums[j+1])
    if res > maxV:
        maxV = res
print(maxV)