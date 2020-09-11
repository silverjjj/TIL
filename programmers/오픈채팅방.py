def solution(record):
    answer = []
    users = {}
    res = []
    for reco in record:
        reco = reco.split(" ")
        key = reco[0]
        ID = reco[1]
        if ID not in users.keys():
            users[ID] = reco[2]
        if key == "Enter":
            answer.append([ID,"님이 들어왔습니다."])
            users[ID] = reco[2]
        elif key == "Leave":
            answer.append([ID, "님이 나갔습니다."])
        elif key == "Change":
            users[ID] = reco[2]
    # print(answer)
    for ID, char in answer:
        res.append(users[ID]+char)
    return res

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)