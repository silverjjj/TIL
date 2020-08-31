'''
results의 각 배열은 A,B를 의미하고 A가 이긴것
[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]의 경우
4 > 3   4 > 2    3 > 2   1 > 2    2 > 5
해당 선수가 이기는 멤버
1 : 2
2 : 5
3 : 2
4 : 3 2
5 :
를 갖고 정확한 순위를 정할수있는 멤버수를 찾자
'''

def solution(n, results):
    win = {i: set() for i in range(1,n+1)}
    lose = {i: set() for i in range(1,n+1)}
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
        print(lose[loser] ,loser)
        # for w in win[loser]:
        #     win[winner].add(w)
        # for l in win[winner]:
        #     lose[loser].add(l)
        print(win)
        print(lose)

    answer = 0
    return answer

n = 5
results = 	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(n, results)