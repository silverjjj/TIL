def solution(answers):
    ans = []
    s = []
    total = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

    for arr in total:
        # print(i)
        num = 10000//len(arr)
        narr = arr * num
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == narr[j]:
                cnt +=1

        s.append(cnt)
    mx = max(s)
    number = 0
    for k in s:
        number +=1
        if mx == k:
            ans.append(number)
    return ans


# answers = [1,3,2,4,2]
answers = [1,2,3,4,5]
print(solution(answers))