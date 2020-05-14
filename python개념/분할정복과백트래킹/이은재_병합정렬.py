# SWex 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬
T = int(input())
for tc in range(1,T+1):
    def merge_sort(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:n])
        return merge(left, right)

    def merge(arr1, arr2):
        global cnt
        result = []
        # print(arr1,arr2)
        flag = 0
        if arr1[-1] > arr2[-1]:
            flag = 1
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
        if flag == 1:
            cnt += 1
        return result

    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    result_arr = merge_sort(arr)
    # print(result_arr)
    print("#{} {} {}".format(tc,result_arr[n//2],cnt))
