# 병합 정렬
def merge_sort(arr):
    # 문제를 절반으로 나누는 함수
    # print(arr)
    if len(arr) == 1:
        # print(arr)
        return arr
    # 절반으로 나누어서 각각 별도의 정렬실행
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge2(left, right)
# def merge(arr1, arr2):    # 나는 이게 더 좋은듯
#     # 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
#     print(arr1,arr2,len(arr)//2)
#     result = []
#     # 각각의 최소값들( 가장 앞쪽 값)을 비교해서 더 작은 요소를
#     # result에 추가
#     # 두 부분집합의 요소가 없어질때까지 반복
#     while arr1 or arr2:
#         # 두 부분집합의 요소가 모두 남아 있을경우
#         if arr1 and arr2:
#             if arr1[0] <= arr2[0]:
#                 result.append(arr1.pop(0))
#             else:
#                 result.append(arr2.pop(0))
#         elif arr1:  # arr1만 남아있을경우
#             result.append(arr1.pop(0))
#         elif arr2:  # arr2만 있을경우
#             result.append(arr2.pop(0))
#     return result
# arr = [2,2,1,1,3]
# print(merge_sort(arr))

# 인덱스를 이동하면서 병합하는 함수
def merge2(arr1,arr2):
    # print(arr1,arr2)
    result = []
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i+=1
            else:
                result.append(arr2[j])
                j+=1
        elif i < len(arr1):
            result.append(arr1[i])
            i+=1
        elif j < len(arr2):
            result.append(arr2[j])
            j+=1
    print(arr1, arr2)
    return result
arr = [5,1,8,9,10,13,4,7]
print(merge_sort(arr))
