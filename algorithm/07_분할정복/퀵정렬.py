def quick_sort(arr, left, right):
    if left < right:  # 오른값이 커야지 진행이 가능
        pivot = hoare_partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    return arr
# 피봇찾기
def hoare_partition(arr, left, right):
    print(arr)
    L = left  # 부분리스트의 가장 앞
    R = right  # 부분리스트의 가장 뒤
    pivot = arr[left]  # 처음 피봇은 가장 앞에있는값으로 시작
    while L <= R:
        while arr[L] <= pivot:
            L += 1
        while arr[R] > pivot:
            R -= 1
        if L < R:
            arr[L], arr[R] = arr[R], arr[L]
    arr[left], arr[R] = arr[R], arr[left]
    return R

arr = [3,2,4,6,9,1,8,7,5]
print(quick_sort(arr,0,len(arr)-1))