import math
def solution(n, stations, w):
    ans = 0
    cur = 1
    for num in stations:
        diff = (num - w) - cur
        ans += math.ceil((diff / (w*2 + 1)))
        cur = num + w + 1
    ans += math.ceil((n - cur + 1) / (w * 2 + 1))
    return ans