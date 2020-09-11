'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로
    더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
'''

ans = ""
def success(u):
    # u가 올바른지 판단
    tmp = 0
    flag = True
    for j in range(len(u)):
        if u[j] == "(":
            tmp += 1
        elif u[j] == ")":
            tmp -= 1
        if tmp < 0:
            flag = False
            break
    return flag

def seperate(p):
    global ans
    if len(p) ==0:
        return
    # 1. 들어온 문자열을 u , v로 나눔
    i = 0
    u = p[0]
    left = right = 0   # ( , )
    if p[i] == "(":
        left += 1
    else:
        right += 1
    while left != right:
        i += 1
        char = p[i]
        u+=char
        if char == "(":
            left += 1
        elif char == ")":
            right += 1
    v = p[i+1:]
    flag = success(u)
    if not flag:
        ans += "("
        seperate(v)
        ans += ")"
        l = len(u)
        u = u[1:l-1]
        for char in u:
            if char == ")":
                ans += "("
            else:
                ans += ")"
    else:
        ans += u
        seperate(v)
    return ans

def solution(p):
    # answer = ''
    answer = seperate(p)
    return answer

p = "(()())()"
solution(p)