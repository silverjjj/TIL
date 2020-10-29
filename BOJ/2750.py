import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr)) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left, right):
    L = R = 0
    sorted_list = []
    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            sorted_list.append(left[L])
            L+=1
        else:
            sorted_list.append(right[R])
            R += 1
    while L < len(left):
        sorted_list.append(left[L])
        L += 1
    while R < len(right):
        sorted_list.append(right[R])
        R += 1
    return sorted_list

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

res = merge_sort(arr)
for num in res:
    print(num)