'''

단어는 2글자 이상
출력은 탈락번호, 몇바퀴
다 돌면 [0,0] 출력
'''

def solution(n, words):
    answer = []
    words.insert(0, "empty")
    L = len(words)
    # cnt = 0
    # M = L // n
    arr = []
    flag = True
    cnt = 1
    while L > cnt+1 and flag:
        print(arr)
        if words[cnt][-1] != words[cnt+1][0] and words[cnt] in arr:
            flag = False
            print(flag)
        elif cnt == 8 and words[cnt+1] in arr:
            flag = False
            print(flag)
        arr.append(words[cnt])
        cnt += 1
    print(cnt,n)
    x = y = 0
    x = cnt % 2
    y = cnt / 2
    print(x,y)

n = 2
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother','robot', 'tank']
# words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
solution(n, words)