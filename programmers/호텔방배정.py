'''
숫자가 너무 커서 리스트로 탐색할수 없을때, 각각의 딕셔너리에 해당 위치를
계속해서 갱신해주면서 풀수있는 문제
'''
def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        # 방이 없을경우
        tmp = room.get(num)
        if not tmp:
            room[num] = num + 1
            answer.append(num)
        # 방이 있을경우
        else:
            # cur = room.get(tmp) # 방이 있으니까 다음방 이동
            arr = [tmp]
            while True:
                next = tmp
                tmp = room.get(tmp) # 이동한 다음방의 방 유무
                # 방이 없는경우 => 방만들고 넣은뒤 break
                if not tmp:
                    room[next] = next + 1
                    answer.append(next)
                    for i in arr:   # 여태까지 거쳐온곳들도 다시 갱신해준다
                        room[i] = next + 1
                    break
                arr.append(tmp)
    return answer

k = 10
room_number = [1,3,4,1,3,1]
solution(k, room_number)