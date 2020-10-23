'''

K 칸 점프하면 에너지 K소모

'''
def solution(d, budget):
    ans = 0
    res = 0
    d.sort()
    print(d)
    n = len(d)
    for idx in range(n):
        res += d[idx]
        if res > budget:
            ans = idx
            break
    return ans
d =[2,2,3,3]
budget = 10
solution(d, budget)