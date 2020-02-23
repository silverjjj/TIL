N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int,input())))
print(nums)

for y in range(0,N//2+1):
    for x in range(N//2,-1,-1):
        nums[y][x:N-2]