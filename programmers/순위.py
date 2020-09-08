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
def updown(win,lose,n,num):
    # print(arr)
    arr = [0] * (n + 1)
    q = [num]
    while q:
        cur = q.pop(0)
        if not arr[cur]:
            arr[cur] = 1
            for next in win[cur]:
                q.append(next)
    q = [num]
    arr[num] = 0
    while q:
        cur = q.pop(0)
        if not arr[cur]:
            arr[cur] = 1
            for next in lose[cur]:
                q.append(next)
    return arr
def solution(n, results):
    answer=0
    win = {i: [] for i in range(1,n+1)}
    lose = {i: [] for i in range(1,n+1)}
    for winner, loser in results:
        win[winner].append(loser)
        lose[loser].append(winner)

    for num in range(1, n + 1):
        arr = updown(win,lose,n,num)
        if sum(arr) == n:
            answer += 1
    # print(answer)
    return answer
n = 5
results = 	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(n, results)