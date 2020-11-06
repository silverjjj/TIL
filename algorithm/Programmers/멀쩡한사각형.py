
from math import gcd

def solution(w,h):
    ans = 0
    nums = w*h
    UDgcd = gcd(w,h)
    N = int(max(w,h)/UDgcd)
    M = int(min(w,h)/UDgcd)
    if M == 1:
        ans = UDgcd * N
    else:
        ans = (w + h - UDgcd)
    return nums-ans

w = 5
h = 3
solution(w,h)

