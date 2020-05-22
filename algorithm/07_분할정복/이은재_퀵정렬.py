# SWex 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬
T = int(input())
for tc in range(1, T + 1):
    def quick_sort(arr, left, right):  # 왼쪽시작점, 오른쪽 시작점
        # pivot의 위치 결정 (피봇을 기준으로 큰값을 오른쪽, 작은건 왼쪽 구분)
        # 왼쪽 정렬
        # 오른쪽 정렬
        if left < right:  # 오른값이 커야지 진행이 가능
            # 피봇 구하기
            pivot = hoare_partition(arr, left, right)
            # print(pivot)
            quick_sort(arr, left, pivot - 1)  # arr = [작은값, 피봇 , 큰값]
            quick_sort(arr, pivot + 1, right)  #

    # 피봇찾기
    def hoare_partition(arr, left, right):
        i = left  # 배열의 가장 앞
        j = right  # 배열의 가장 뒤
        pivot = arr[left]  # 처음 피봇은 가장 앞에있는값으로 시작

        # i가 j값보다 작을 때까지 진행
        while i <= j:
            # 피봇 보다 큰값이 나올때 까지 i증가
            while i <= j and arr[i] <= pivot:  # i <= j 는 i가 계속커져서 j를 넘어설경우를 방지
                i += 1
            # 피봇보다 작은 값이 나올때 까지 j 감소
            while i <= j and arr[j] >= pivot:  # i <= j : j 가 감소하여 i 값보다 작아지는걸 방지
                j -= 1
            # 위 두 while 문이 끝났다는것은 i는 pivot보다 크고, j는 pivot보다 작은값이 된상태
            # 그럴경우 i가 j보다 작기때문에, 위치교환
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        # 큰 while문이 끝나면 arr는 arr = [pivot, 작은값(i~j), 큰값] 상태가 된다. 피봇을 가운데로 보내기 위해
        arr[left], arr[j] = arr[j], arr[left]
        return j

    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print("#{} {}".format(tc, arr[n // 2]))