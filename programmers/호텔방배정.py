# 리스트는
def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        stan = room.get(num,0)
        # print("stan ==> ",stan,"num ==>",num)
        if stan:
            for i in range(stan+1,k+1):
                tmp = room.get(i, 0)
                print("qqqqqqqq")
                if not tmp:
                    room[i] = num
                    answer.append(i)
                    print(i)
                    break
            print("sss")

        else:
            room[num] = num
            answer.append(num)
    return answer

k = 10
room_number = [1,3,4,1,3,1]
solution(k, room_number)