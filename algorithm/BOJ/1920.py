import sys
input = sys.stdin.readline
def binary_search(num):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if num == arr[mid]:
            return 1
        elif num > arr[mid]:
            left = mid + 1
        elif num < arr[mid]:
            right = mid - 1
    return 0

N = int(input())
arr = list(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))
arr.sort()
res = 0
for num in nums:
    print(binary_search(num))
