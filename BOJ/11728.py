'''
병합정렬
'''
import sys
input = sys.stdin.readline

# 1. 분할
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# 2. 합병
def merge(left, right):
    l = r = 0
    sorted_list = []
    # 두 배열을 비교하면서 sort를 진행
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
    # 남은 값들을 넣어줌
    while l < len(left):
        sorted_list.append(left[l])
        l += 1
    while r < len(right):
        sorted_list.append(right[r])
        r += 1
    return sorted_list

N, M = map(int,input().split())
left = list(map(int,input().split()))
right = list(map(int,input().split()))
arr = merge(left, right)
for num in arr:
    print(num, end = " ")