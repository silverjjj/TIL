import math
def solution(pro, sp):
    ans = []
    n = len(pro)
    s = []
    for i in range(n):
        if ((100 - pro[i]) % sp[i]) == 0:
            s.append((100 - pro[i]) // sp[i])
        else:
            s.append((100 - pro[i]) // sp[i]+1)
    print(s)
    first = 0
    for j in range(len(s)):
        if s[first] < s[j]:
            ans.append(j-first)
            first = j
    # 밑에 있는게 핵심이다!!!
    ans.append(len(s)-first)
    return ans
pro = [93,30,55]
sp = [1,30,10]
print(solution(pro,sp))