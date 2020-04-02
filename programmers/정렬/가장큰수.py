sum = ''
def solution(numbers):
    num = list(map(str,numbers))
    maxV = 0
    visit = [0] * len(numbers)
    p = [0] * len(numbers)
    find(0, len(num))
    return maxV

def find(n,k):
    global visit, p, num, maxV
    if n == k:
        sum = ''
        for j in p:
            sum += j
        sum = int(sum)
        if sum > int(maxV):
            maxV = str(sum)
    else:
        for i in range(k):
            if visit[i] == 0:
                p[n] = num[i]
                visit[i] = 1
                find(n+1,k)
                visit[i] = 0





