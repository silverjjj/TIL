cnt = 0
def BFS(n, money,res):
    global cnt
    print(n,res,cnt)
    if res == n:
        cnt += 1
        return
    if res > n:
        return
    for won in money:
        print(won)
        BFS(n, money, res + won)

    return cnt

def solution(n, money):
    answer = 0
    print(BFS(n, money,0))

    return answer
n = 5
money = [1,2,5]
solution(n, money)
