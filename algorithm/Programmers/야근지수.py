"""
최대힙을 구현할줄 알아야하는게 중요
"""
import heapq
def solution(n, works):
    answer = 0
    hq = []
    for work in works:
        heapq.heappush(hq,(-work,work))
    if n >= sum(works):
        return 0

    for idx in range(n):
        x,y = heapq.heappop(hq)
        heapq.heappush(hq, (-(y-1), y-1))
    for _x,_y in hq:
        answer += (_y ** 2)
    return answer