def DFS(n,r,tr,nums):
    global arr
    if r == 0:
        arr.append(sum(tr))
    elif n < r:
        return
    else:
        tr[r-1] = nums[n-1]
        DFS(n-1,r-1,tr,nums)
        DFS(n-1,r,tr,nums)

def solution(nums):
    global arr
    tr = [0] * 3
    n = len(nums)
    DFS(n, 3,tr,nums)
    res = 0
    for num in arr:
        for i in range(2, num):
            if not num % i:
                res += 1
                break
    # print(len(arr) - res)
    return len(arr) - res
arr = []
nums = [1,2,7,6,4]
solution(nums)