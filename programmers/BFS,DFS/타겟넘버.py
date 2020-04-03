# dfs 재귀 문제
# 내가 dfs는 스택 or 큐로만 푸려는 습관이 있는데
# 재귀로도 푸는 문제가 나올수 있다
def solution(num, tar):
    ans = 0
    def find(num,tar,idx):
        if len(num) > idx:
            # print(num)
            num[idx] *= 1
            find(num,tar,idx+1)
            # print(num)
            num[idx] *=-1
            find(num, tar, idx + 1)
        elif sum(num) == tar:
            nonlocal ans
            ans +=1
    # idx는 num내 인덱스배열순서
    find(num,tar,0)
    return ans


num = [1, 1, 1, 1, 1]
tar = 3
print(solution(num, tar))
