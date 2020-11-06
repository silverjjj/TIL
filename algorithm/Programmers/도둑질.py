def maxMoney(money):
    answer = 0
    n = len(money)
    visited = [0]*n
    visited[0] = money[0]
    visited[1] = money[1]
    for i in range(n-2):
        if visited[i] + money[i+2] > visited[i+2]:
            visited[i + 2] = visited[i] + money[i+2]
        if i == n-3:
            continue
        if visited[i] + money[i + 3] > visited[i + 3]:
            visited[i + 3] = visited[i] + money[i + 3]

    if visited[-1] >= visited[-2]:
        answer = visited[-1]
    else:
        answer = visited[-2]
    # print(answer)
    return answer

def solution(money):
    ans1 = maxMoney(money[:-1])
    ans2 = maxMoney(money[1:])
    # print(ans1,ans2)
    if ans1 > ans2:
        return ans1
    else:
        return ans2
money = [1,2,3,1,5,3,2,4,2,1,2,5,56,3,42,3,43,2,4,3,5]
solution(money)