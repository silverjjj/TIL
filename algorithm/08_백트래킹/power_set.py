# 백트래킹을 이용한 멱집합(power_set)구하기
def backtrack(selected,idx,input):
    # selected : 각 노드의 선택여부를 판단하는 배열
    # idx : 깊이
    # input : 목표개수
    print(selected)
    candidates = [0]*2 # 선택할 수 있는 선택지는 o/x
    if idx == input:
        for i in range(input):
            if selected[i]:
                print(arr[i],end = " ")
        print()
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
arr=['a','b','c','d','e']
n = 5
backtrack([0]*n,0,n)
