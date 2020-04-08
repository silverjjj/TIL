def solution(skill, skill_trees):
    answer =
    for skt in skill_trees:
        tmp = ""
        re = True
        for s in skt:
            if skill.find(s) != -1:  # 문자열 find는 해당 숫자가 없을경우 -1를 출력
                tmp += s
        # print(tmp, skt)
        for j in range(len(tmp)):
            if tmp[j] != skill[j]:
                re = False
                break
        if re == True:
            answer += 1

    return answer

skill = "CBD"
skill_trees= ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))