def solution(k, room_number):
    answer = []
    room = {}
    # room = {i : [] for i in range(1,k+1)}
    for num in room_number:
        while True:
            if num not in list(room.keys()):
                room[num] = num+1
                answer.append(num)
                break
            num = room[num]
    return answer
k = 10
room_number = [1,3,4,1,3,1]
solution(k, room_number)