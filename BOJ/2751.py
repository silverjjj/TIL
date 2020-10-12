import sys
input = sys.stdin.readline

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    under, equal, up = [], [], []
    for num in arr:
        if num < pivot:
            under.append(num)
        elif num > pivot:
            up.append(num)
        else:
            equal.append(num)
    return quick_sort(under) + equal + quick_sort(up)

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(quick_sort(arr))