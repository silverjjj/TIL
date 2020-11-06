# 1. 분할
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_sort(left, right)

# 2. 합병
def merge(left, right):
    l = r = 0
    sorted_list = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r+=1
    while l < len(left):
        sorted_list.append(left[l])
        l += 1
    while r < len(right):
        sorted_list.append(right[r])
        r += 1
    return sorted_list

def solution(A, B):
    answer = 0
    A = merge_sort(A)
    B = merge_sort(B)
    if A[0] >= B[-1]:
        return 0
    while A:
        maxA = A[-1]
        maxB = B[-1]
        if maxA < maxB:     # 각 배열의 최댓값끼리 대결
            answer += 1
            B.pop(-1)
            A.pop(-1)
        else:
            A.pop(-1)
    # print(answer)
    return answer

A = [2,2,2,2]
B =[1,1,1,1]
solution(A, B)
