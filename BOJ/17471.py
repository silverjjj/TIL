# 백트래킹을 이용한 멱집합(power_set)구하기
def backtrack(selected,idx,input):
    candidates = [0]*2 # 선택할 수 있는 선택지는 o/x
    if idx == input:
        tmp1 = []; tmp2 = []
        for i in range(input):
            if selected[i]:
                tmp1.append(i)
            else:
                tmp2.append(i)
        lst.append([tmp1[:],tmp2[:]])
        return
    else:
        n_candidate=make_condidata(candidates) # 후보군생성
        for i in range(n_candidate):
            selected[idx] = candidates[i]
            backtrack(selected,idx+1,input)

def make_condidata(candidates):
    candidates[0] = 1
    candidates[1] = 0
    return 2
lst = []
arr=['a','b','c','d','e']
n = 5
backtrack([0]*n,0,n)
print(lst)