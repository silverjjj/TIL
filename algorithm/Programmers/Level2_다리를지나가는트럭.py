
def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = tmp = 0
    s = []
    for i in truck_weights:
        s.append(i)
            # print(tmp)
        print(s)
        while s:
            if sum(s) >= weight:
                tmp = s.pop()
            print(s)
            cnt +=1
            if cnt == bridge_length:
                s.pop()
                answer += bridge_length
                cnt = 0
        if tmp != 0:
            s.append(tmp)

    return answer

bridge_length = 2
weight = 10
truck_weights=[7,4,5,6]
print(solution(bridge_length,weight,truck_weights))