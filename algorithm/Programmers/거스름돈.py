answer = 0
def BFS(n, money,res):
    global answer
    print(n,res)
    if res == n:
        answer += 1
        print(res)
        return
    elif res > n:
        return
    else:
        for won in money:
            print('won>>',won)
            BFS(n, money, res + won)
def solution(n, money):
    BFS(n, money,0)
    print(answer)
    return answer
n = 5
money = [1,2,5]
solution(n, money)
