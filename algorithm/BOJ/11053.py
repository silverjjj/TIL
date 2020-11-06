N = int(input())
nums = list(map(int,input().split()))
weight = [0] * (max(nums) + 1)
for num in nums:
    weight[num] = max(weight[:num]) + 1
print(max(weight))