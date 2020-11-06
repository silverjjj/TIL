import heapq
def solution(operations):
    hq = []
    for oper in operations:
        if oper[0] == "I":
            heapq.heappush(hq,int(oper[2:]))
        else:
            if len(hq) >= 1:
                if oper[2] == "1":
                    heapq._heapify_max(hq)
                    s = heapq._heappop_max(hq)
                else:
                    heapq.heapify(hq)
                    s = heapq.heappop(hq)
    if len(hq) > 1:
        hq.sort()
        ans = [hq[-1],hq[0]]
    else:
        ans = [0,0]
    return ans