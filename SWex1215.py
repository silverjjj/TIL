N = int(input())
nums = [list(input()) for _ in range(8)]

print(nums)
print((nums[0][0:4]))
cnt =0
# for i in range(8-N+1):
#     for j in range(8-N+1):
#         if nums[i][j:(N//2)+j] != nums[i][j+(N//2):N+j]:
#             continue
#         cnt +=1

print(cnt)