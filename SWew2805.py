N = int(input())


nums = []
for i in range(N):
    nums.append(list(map(int,input().strip())))
h = N//2
print(nums)
sum = 0
cnt = 1
for i in range(N):                  #   가로
    if i <= h:
        for j in range(h-i,h+i+1):       #세로
            sum += nums[i][j]
    
    else:
        for j in range(i-h,h+i-cnt):
            sum += nums[i][j]
        cnt +=1
print(sum)