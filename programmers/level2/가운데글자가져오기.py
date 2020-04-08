def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        n = len(s) // 2
        answer += s[n]
    else:
        n = (len(s) // 2) - 1
        answer += s[n:n+2]
    # print(n,answer)
    return answer
s = "asca"
print(solution(s))