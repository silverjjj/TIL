'''
BOJ 1107
5% 에서 틀림
'''
def conbination(depth,arr,visited,nums,L):
    if depth == L:
        # print(int(N)-int(nums), int(nums)-int(N))
        # print(nums,abs(int(N) - int(nums)),len(nums))
        print(nums)
        res.append(abs(int(N) - int(nums)) + len(str(int(nums))))
        return
    else:
        for i in range(len(N)):
            if not visited[i]:
                visited[i] = 1
                for num in arr[i]:
                    nums += str(num)
                    conbination(depth+1, arr, visited, nums,L)
                    nums = nums[:-1]
                visited[i] = 0
                return

N = str(input())
M = int(input())
remove = []
res = [abs(int(N) - 100)]
if M != 0:  # 1~ 9일땐 제거를 받고
    remove = list(map(int,input().split()))
remote = [1,1,1,1,1,1,1,1,1,1]

for num in remove:
    remote[num] = 0
arr = []
for num in N:
    num = int(num)
    if remote[num]:
        arr.append(num)
    else:
        tmp_num = num
        tmp_num -= 1
        while tmp_num >= 0:
            if remote[tmp_num]:
                arr.append(tmp_num)
                break
            tmp_num -= 1

        tmp_num = num
        tmp_num += 1
        while tmp_num <= 9:
            if remote[tmp_num]:
                arr.append(tmp_num)
                break
            tmp_num += 1
print(arr)
nums = ""
visited = [0 for _ in range(len(N))]
for i in range(1, len(N)+1):
    conbination(0,arr,visited,nums,i)
print(res)
print(min(res))


'''

5457
4
5 7 8

0
4
0 1 2 3

1
4
0 1 2 3

500000
10
0 1 2 3 4 5 6 7 8 9


101
3
4 5 6

1

162
9
0 1 3 4 5 6 7 8 9

62

1555
8
0 1 3 4 5 6 7 9

670
'''