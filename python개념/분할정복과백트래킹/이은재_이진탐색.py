# SWex 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    arr2 = list(map(int,input().split()))
    cnt = 0
    for key in arr2:
        start = 0
        end = n - 1
        left = right = 0
        while start <= end:  # end값이 더 클때만 true
            mid = (start + end) // 2
            if arr[mid] == key:    # 탐색 완료
                if left <= 1 and right <=1:
                    cnt += 1
                break
            elif arr[mid] > key:
                end = mid - 1
                left += 1
                if left >= 2:
                    break
                if right != 0:
                    right -=1

            elif arr[mid] < key:
                start = mid + 1
                right += 1
                if right >= 2:
                    break
                if left != 0:
                    left -=1

    print("#{} {}".format(tc,cnt))