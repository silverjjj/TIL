def solution(cookie):
    n = len(cookie)
    maxV = 0
    for i in range(n - 1):
        cur1 = i
        cur2 = i + 1
        son1 = cookie[cur1]
        son2 = cookie[cur2]
        flag = True
        while flag:
            if son1 == son2:
                if son1 > maxV:
                    maxV = son1
            if son1 < son2:
                if 0 <= cur1 - 1 < n:
                    cur1 -= 1
                    son1 += cookie[cur1]
                else:
                    flag = False
            elif son1 > son2:
                if 0 <= cur2 + 1 < n:
                    cur2 += 1
                    son2 += cookie[cur2]
                else:
                    flag = False
            else:
                if 0 <= cur1 - 1 < n and 0 <= cur2 + 1 < n:
                    cur1 -= 1;
                    cur2 += 1
                    son1 += cookie[cur1]
                    son2 += cookie[cur2]
                else:
                    flag = False
    return maxV