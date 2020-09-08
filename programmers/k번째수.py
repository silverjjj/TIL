def solution(arr, com):
    answer = []
    arr.insert(0, 0)
    for i in range(len(com)):
        tmp = arr[com[i][0]:com[i][1]+1]
        tmp.sort()
        # print(tmp)
        num = tmp[com[i][2]-1]
        answer.append(num)
    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(arr,com)