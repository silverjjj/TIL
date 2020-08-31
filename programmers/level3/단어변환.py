'''
hit 시작
hot i -> o
dot h -> d
dog t -> g
cog d -> c
한번에 한개의 알파벳만 변경
'''
def solution(begin, target, words):
    answer = 0
    if target not in tuple(words):
        return answer
    s = []
    s.append(begin)
    visited = [0 for _ in words]
    while s:
        print(visited,s)
        begin = s.pop()
        if begin == target:
            return answer
        for w in range(len(words)):
            if len([i for i in range(len(words[w])) if words[w][i] != begin[i]]) == 1:
                if visited[w] != 0:
                    continue
                visited[w] = 1
                s.append(words[w])
        answer += 1
begin = "hit"
target = "cog"
words = ['dot', 'dog', 'lot', 'log', "cog", 'hot', 'hut']
print(solution(begin, target, words))