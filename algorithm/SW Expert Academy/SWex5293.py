# SWex5293. 이진 문자열 복원

# def f(n,k):
#     global result
#     if n == k:
#         return
#
#     for i in range(1,k):
#         if result[0][-1] == rm[i][0]:
#             result.append(rm[i])
#         elif result[0][0] == rm[0][i]:
#             result.insert(0,rm[0][i])
#
bit = ['00','01','10','11']
num = list(map(int ,input().split()))
rm = []
result = []
c= 0
for i in range(4):
    for j in range(num[i]):
        rm.append(bit[i])
print(rm)
print(type(rm))
for i in range(len(rm)):
    rm[i] = str(rm[i])
# print(rm[0])
# print(type(rm[0]))
result.append(rm[0])
# f(0,len(rm))
k = len(rm)
for i in range(1, k-1):
    # print(result)
    if result[0+c][-1] == rm[i][0]:
        result.append(rm[i])
        c +=1
    # elif result[0][0] == rm[0][i]:
    #     result.insert(0, rm[0][i])
print(result)
print(rm)
nrm = []
if result not in rm:
    
print(nrm)