def SelectionSort(num,k):
    n = len(num)
    if k == n-1:
        return
    minV = k
    for i in range(k,n):
        if num[minV] > num[i]:
            num[k], num[k+1] = num[k+1],num[k]
    SelectionSort(num,k+1)
num = [4,3,7,5,5,3,2,6,8,0,3,0,12,421,21]
SelectionSort(num,0)
print(num)
