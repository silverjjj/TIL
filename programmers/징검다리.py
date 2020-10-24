def solution(distance, rocks, n):
    ans = 0
    rocks.sort()
    left = 0
    right = distance
    while left <= right:
        mid = (left + right) // 2
        pre = 0     # 출발지점
        minV = float('inf')
        removed_rock = 0
        for rock in rocks:
            if mid > rock - pre:
                removed_rock += 1
            else:
                minV = min(minV, rock - pre)
                pre = rock
        if removed_rock > n:
            right = mid - 1
        else:
            left = mid + 1
            ans = minV
    return ans