def solution(numbers):
    answer = 0
    k = len(numbers)
    print(k)
    visit = [0]*k
    num = [0]*k
    total = []
    # 우선 순열로 모든 숫자를 만들자
    def p(n,k):
        nonlocal num
        if n == k:
            sum = ""
            for j in num:
                sum += j
            if sum not in total:
                total.append(sum)
        else:
            for i in range(k):
                if visit[i] == 0:
                    num[n] = numbers[i]
                    visit[i] = 1
                    p(n+1,k)
                    visit[i] = 0
    p(0,k)
    print(total)
    return answer


numbers = "011"
solution(numbers)