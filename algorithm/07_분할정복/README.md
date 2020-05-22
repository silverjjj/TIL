# 분할정복과 백트래킹

> * 분할정복 => 퀵정렬, 병합정렬
>
> * 백트래킹
>
> * 이진트리 => 탐색, 삽입, 삭제

## 1. 분할정복 (Devide and Conque)

> 분할정복을 이용한 대표적인 정렬알고리즘인 병합정렬과 퀵정렬에 대해 알아볼것이다.
>
> 실제 전략 : 분할 => 정복 => 통합과정으로 이루어진다

### 1). 병합정렬

* 정렬된 자료의 집합을 한 개의 정렬된 집합으로 만드는 정렬 알고리즘
  * ex) 6 2 5 1 => 26 15 => 1256
    * 자료를 최소단위로 나눈후에 차례

#### 소스코드

##### 방법 1. append와 pop을 이용한 방법

```python 
# 분할과정
def merge_sort(arr):
    # 문제를 절반으로 나누는 함수
    # print(arr)
    if len(arr) == 1:
        print(arr)
        return arr
    # 절반으로 나누어서 각각 별도의 정렬실행
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
# 병합과정
def merge(arr1, arr2):
    # 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
    print(arr1,arr2,len(arr)//2)
    result = []
    # 각각의 최소값들( 가장 앞쪽 값)을 비교해서 더 작은 요소를
    # result에 추가
    # 두 부분집합의 요소가 없어질때까지 반복
    while arr1 or arr2:
        # 두 부분집합의 요소가 모두 남아 있을경우
        if arr1 and arr2:
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif arr1:  # arr1만 남아있을경우
            result.append(arr1.pop(0))
        elif arr2:  # arr2만 있을경우
            result.append(arr2.pop(0))
    return result
arr = [5,1,8,9,10,13,4,7]
print(merge_sort(arr))
```



##### 방법 2. 인덱스를 활용한 방법 : 이 방법이 더 빠름.

```python
# 분할과정
def merge_sort(arr):
    # 문제를 절반으로 나누는 함수
    # print(arr)
    if len(arr) == 1:
        print(arr)
        return arr
    # 절반으로 나누어서 각각 별도의 정렬실행
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
# 인덱스를 이동하면서 병합하는 함수
# 병합과정
def merge2(arr1,arr2):
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
    print(arr1,arr2)
    return result
arr = [5,1,8,9,10,13,4,7]
print(merge_sort(arr))
######## print 출력 #######################
[5] [1]
[8] [9]
[1, 5] [8, 9]
[10] [13]
[4] [7]
[10, 13] [4, 7]
[1, 5, 8, 9] [4, 7, 10, 13]
[1, 4, 5, 7, 8, 9, 10, 13]
```



### 2). 퀵정렬(Quick Sort)

> 병합정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준아이템(pivot item) 중심으로, 작은것은 왼편, 큰것은 오른편이 위치시킨다.

```python
# 알고리즘
qucikSort(arr,l,r)
	if l < r:
        s <-partition(a,l,r)	# pivot의 위치를 결정
        qucikSort(arr,l,s-1)	# pivot보다 작은 값들
        qucikSort(arr,s+1,r)	# pivot보다 큰 값들

'''
퀵정렬은 병합정렬(nlogn)보다 빠르지만 pivot의 최악의 경우 최대 n^2의 시간복잡도를 갖는다.
'''
```



#### 피봇을 찾는 알고리즘

#### Hoare-Partition 알고리즘

```python
# 1. pivot구하는 알고리즘, 호어의 교환 횟수가 로무토에 비해 1/3정도,,, 
def hoare_partition(arr, left, right):
    i = left  # 배열의 가장 앞
    j = right  # 배열의 가장 뒤
    pivot = arr[left]  # 처음 피봇은 가장 앞에있는값으로 시작

    # i가 j값보다 작을 때까지 진행
    while i <= j:
        # 피봇 보다 큰값이 나올때 까지 i증가
        while arr[i] <= pivot:  # i <= j 는 i가 계속커져서 j를 넘어설경우를 방지
            i += 1
        # 피봇보다 작은 값이 나올때 까지 j 감소
        while arr[j] > pivot:  # i <= j : j 가 감소하여 i 값보다 작아지는걸 방지
            j -= 1
        # 위 두 while 문이 끝났다는것은 i는 pivot보다 크고, j는 pivot보다 작은값이 된상태
        # 그럴경우 i가 j보다 작기때문에, 위치교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 큰 while문이 끝나면 arr는 arr = [pivot, 작은값(i~j), 큰값] 상태가 된다. 피봇을 가운데로 보내기 위해
    arr[left], arr[j] = arr[j], arr[left]
    return j
arr = [7,5,4,1 ,2 ,10 ,3 ,6 ,9 ,8,]
quick_sort(arr,0,len(arr)-1)
'''
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
            대신 
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
            도 가능
            '''
```

#### Lomuto partition 알고리즘

```python
# 1. pivot 구하는 알고리즘
def lomuto_partition(arr,left, right):
    pivot = arr[right]	# 맨 마지막값
    i = left -1
    j = left
    for j in range(left,right):
        # arr[j]가 pivot보다 작으면,
        if arr[j] < pivot:
        # i 를 1 증가
        # arr[j] , arr[i] 위치교환
        i +=1
        arr[i], arr[j] = arr[j], arr[i]
    
    # i가 가리키는 위치가 pivot보다 작은 값의 마지막 index
    # i+1의 위치에 pivot을 두고 i+1 반환
	arr[i+1], arr[right] = arr[right],arr[i+1]
    return i+1 # pivot의 index
```



#### 퀵정렬 소스코드

>구현과정이 복잡하니 유튜브를 참고하자(유튜브에 자세히 나와있음)

```python 
def quick_sort(arr, left, right):  # 왼쪽시작점, 오른쪽 시작점
    # pivot의 위치 결정 (피봇을 기준으로 큰값을 오른쪽, 작은건 왼쪽 구분)
    # 왼쪽 정렬
    # 오른쪽 정렬
    if left < right:  # 오른값이 커야지 진행이 가능
    # 피봇 구하기
        pivot = hoare_partition(arr, left, right)
        print(pivot)
        quick_sort(arr, left, pivot - 1)  # arr = [작은값, 피봇 , 큰값]
        quick_sort(arr, pivot + 1, right)  #

# 2. pivot구하는 알고리즘, 호어의 교환 횟수가 로무토에 비해 1/3정도,,, 
def hoare_partition(arr, left, right):
    print(arr)
    i = left  # 배열의 가장 앞
    j = right  # 배열의 가장 뒤
    pivot = arr[left]  # 처음 피봇은 가장 앞에있는값으로 시작
    # i가 j값보다 작을 때까지 진행
    while i <= j:
        # 피봇 보다 큰값이 나올때 까지 i증가
        while arr[i] <= pivot:  # i <= j 는 i가 계속커져서 j를 넘어설경우를 방지
            i += 1
        # 피봇보다 작은 값이 나올때 까지 j 감소
        while arr[j] > pivot:  # i <= j : j 가 감소하여 i 값보다 작아지는걸 방지
            j -= 1
        # 위 두 while 문이 끝났다는것은 i는 pivot보다 크고, j는 pivot보다 작은값이 된상태
        # 그럴경우 i가 j보다 작기때문에, 위치교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 큰 while문이 끝나면 arr는 arr = [pivot, 작은값(i~j), 큰값] 상태가 된다. 피봇을 가운데로 보내기 위해
    arr[left], arr[j] = arr[j], arr[left]
    return j	# 피봇을 quick_sort 함수에 리턴
arr = [3,2,4,6,9,1,8,7,5]
quick_sort(arr,0,len(arr)-1)
print(arr) 맨처음 피봇 index는 0
[3, 2, 4, 6, 9, 1, 8, 7, 5]
4<->1
[1, 2, 3, 6, 9, 4, 8, 7, 5]
1<->3
[1, 2, 3, 6, 9, 4, 8, 7, 5]
[1, 2, 3, 4, 5, 6, 8, 7, 9]
6<->4 => 9<->5
[1, 2, 3, 4, 5, 6, 8, 7, 9]
8<->7
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```



### 3. 이진검색(Binary Search)

> 1. 자료의 중앙의 원소를 고른다.
> 2. 중앙 원소값과 찾고자 하는 목표값을 비교
> 3. 목표값이 중앙원소값보다 작으면 왼쪽, 크다면 오른쪽을 찾는다.
> 4. 1~3번은 반복
>
> 결론 : 중앙 원소값이 계속 변하면서 반씩 나누고, 나누고 하면서 목표값을 찾는과정 => 이진탐색

#### 이진탐색 소스코드

```python
# 이진탐색 : 반복 구조
def binarySearch(arr, key):
    start = 0
    end = n - 1
    mid = (start + end) // 2
    while start <= end:  # end값이 더 클때만 true
        print(arr[start],arr[end])
        mid = (start + end) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
    return False
arr = [4, 7, 8, 10, 12, 13, 15, 17, 20, 21, 35]
n = len(arr)
print(binarySearch(arr,15))

# 이진탐색 : 재귀구조
def binarySearch2(arr,key,start,end):
    if start > end
    	return -1
    else:
        mid = (low+high)//2
        if key == arr[mid]:
        	return 1
        elif key < arr[mid]:
        	return binarySearch2(arr,key,start,arr[mid]-1 )
        else:
            return binarySearch2(arr,key,arr[mid]+1,end )
    binarySearch2`
```

