# 이진탐색 : 반복 구조
def binarySearch(arr, key):
    start = 0
    end = n - 1
    cnt = 0
    while start <= end:  # end값이 더 클때만 true
        cnt +=1
        mid = (start + end) // 2
        if arr[mid] == key:
            return True,cnt
        elif arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
    return False,cnt

# 이진탐색 : 재귀구조
def binarySearch2(arr,key,start,end,cnt2):
    print(arr)
    if start > end:
        return False,cnt2
    else:
        mid = (start + end)//2
        if key == arr[mid]:
            return True, cnt2
        elif key < arr[mid]:
            return binarySearch2(arr,key,start,mid-1,cnt2+1)
        else:
            return binarySearch2(arr,key,mid+1,end,cnt2+1)


arr = [4, 7, 8, 10, 12, 13, 15, 17, 20, 21, 35]
n = len(arr)
print(binarySearch(arr,15))
print(binarySearch2(arr,15,0,n-1,0))