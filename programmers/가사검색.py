words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = [0]*len(queries)

    for q in range(len(queries)):
        for word in words:
            if len(word) == len(queries[q]):
                idx = queries[q].index("?")

                if idx == 0:
                    for i in range(len(queries[q])):
                        if "?" != queries[q]:
                            print(i)
                            if queries[q][i:] == word[i:]:
                                answer[q] += 1
                else:
                    if queries[q][:idx] == word[:idx]:
                        print(idx)
                        answer[q] += 1
    return answer

print(solution(words, queries))