def solution(A, B):
    answer = 0
    dictB = {}
    listB = []
    for num in B:
        if num in dictB.keys():
            dictB[num] += 1
        else:
            dictB[num] = 1
            listB.append(num)
    listB.sort()
    res = 0
    for a in A:
        if listB[-1] > a:
            idx = listB.index(a)
            nexta = listB[idx+1]
            if nexta in dictB.keys():
                dictB[nexta] -= 1
                res += 1
                if dictB[nexta] == 0:
                    listB.remove(nexta)
                    del dictB[nexta]

        else:
            break
    print(res)
    return res

A = [5,1,3,7]
B = [2,2,6,8]
# A = [2,2,2,2]
# B = [1,1,1,1]
solution(A, B)