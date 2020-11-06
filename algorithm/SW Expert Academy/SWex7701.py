# SWex7701. 염라대왕의 이름 정렬
for tc in range(int(input())):
    n = int(input())
    rm = [[]*n for _ in range(n)]
    for i in range(n):
        w = input()
        rm[len(w)].append(w)
    new_rm = []
    for row in rm:
        result = set(row)
        result = list(result)
        result.sort()
        new_rm.append(result)
    print("#{}".format(tc+1))
    for i in range(len(new_rm)):
        for j in range(len(new_rm[i])):
            print(new_rm[i][j])


