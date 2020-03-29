def solution(p, l):
    ans = 0
    s = []
    # location에 대한 특별한 표식 -> str
    p[l] = str(p[l])
    value = p[l]
    # print(value)
    while len(p) != 0:
        # print(s,priorities)
        for i in range(1,len(p)):
            if int(p[0]) < int(p[i]):
                tmp = p.pop(0)
                p.append(tmp)
                break
        else:   # 배열의 맨앞를 모든 배열과 비교해서 클경우 s에 할당
            s.append(p[0])
            p.pop(0)       #맨 앞에를 pop한다.
    # print(s,value)
    for k in range(len(s)):
        if s[k] == value:
            ans = k+1
    return ans
# priorities = [2, 1, 3, 2]
priorities =[1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))

