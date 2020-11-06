
def find(s ,k ,i):
    arr = []
    char = s[:i]
    cnt = 1
    for j in range(i,k,i):
        if char == s[j:j+i]:
            cnt += 1
        else:
            arr.append([cnt, char])
            char = s[j:j+i]
            cnt = 1
    arr.append([cnt, char])
    res = 0
    for num, chars in arr:
        res += len(chars)
        if num != 1:
            res += len(str(num))
    return res
def solution(s):
    k = len(s)
    minV = 1000
    for i in range(1,k+1):
        res = find(s ,k ,i)
        if minV > res:
            minV = res
    return minV
s = 'ababcdcdababcdcd'
solution(s)