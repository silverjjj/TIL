import sys
input = sys.stdin.readline

arr1 = [0] + list(input())
arr2 = [0] + list(input())
arr1.pop(-1); arr2.pop(-1)
# print(arr1,arr2)
rm = [[str(0)] * (len(arr1)) for _ in range(len(arr2))]
maxV = 0
for i in range(1,len(arr2)):
    for j in range(1,len(arr1)):
        if arr1[j] == arr2[i]:
            rm[i][j] = rm[i-1][j-1] + arr2[i]
        else:   # 다를때
            if len(rm[i-1][j]) >= len(rm[i][j-1]):
                rm[i][j] = rm[i-1][j]
            elif len(rm[i-1][j]) < len(rm[i][j-1]):
                rm[i][j] = rm[i][j-1]
    if len(rm[i][j]) > maxV:
        maxV = len(rm[i][j])
# for r in rm:
#     print(r)
print(maxV - 1)