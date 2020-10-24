'''
이분탐색문제
'''
def solution(n, times):
    right = max(times) * n
    left = 0
    mid = (right + left) // 2
    ans = 0
    while left <= right:
        person = 0
        for time in times:
            person += (mid // time)
            if person > n:
                break
        if person >= n:
            right = mid - 1
            ans = mid
        elif person < n:
            left = mid + 1
        mid = (right + left) // 2
    return ans