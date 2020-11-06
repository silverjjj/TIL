def solution(heights):
    answer = []
    # heights.reverse()
    n = len(heights) - 1
    for i in range(n,-1,-1):
        for j in range(i-1,-1,-1):
            if heights[j] > heights[i]:
                answer.append(j+1)
                # print(answer)
                break
        else:
            answer.append(0)
    answer.reverse()
    return answer


heights = [5,4,3,2,1]

print(solution(heights))