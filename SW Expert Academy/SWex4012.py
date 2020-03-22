import itertools

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]
n = N//2
nu = []
for i in range(N):
    nu.append(str(i))
# print(num,n)
new_num = list(map("".join, itertools.combinations(nu,n)))
use = [[0]*n for _ in range(len(new_num))]
result = sum1 = sum2 = 0
minV = 987654
# print(new_num)
# # 조합으로 출력된 숫자들을 int형으로 변환
for i in range(len(new_num)):
    for j in range(0,n):
        use[i][j] = int(new_num[i][j])
# print(nu)
print(use)
num = [0]*n

for i in range(len(use)):

    for j in range(n):
        # for a in range(N):
        #     num[i] = int(nu[a])
        #         print(num)
        sum1 += (S[i][j] + S[j][i])
        num.pop(use[i][j])
        for k in range(len(num)):
            for l in range(k,len(num)):
                sum2 +=(S[k][l] + S[k][l])
                result = abs(sum1-sum2)
                if minV > result:
                    minV = result

print(minV)



#
#         use[i][j] = int(new_num[i][j])
# print(use)
#
# for i in range(N):
#     num[i] = int(num[i])
# for i in range(len(use)):
#     for j in range(n):
#         use[i][j]+ use[][]