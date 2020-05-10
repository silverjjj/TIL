# # 재귀를 이용한 부분집합
arr = [1,2,3,4,5,6]
N = len(arr)
bit = [0]*N
cnt=0
def subset(k):    # k :함수호출의 깊이, n : 호출트리의 높이, 단말노드드
    global cnt
    if k == N:
        cnt+=1
        print(bit,cnt)
        return
    # return을 해도되고 안해도된다. why ?? 어차피 어떠한 조건하에 재귀가 다 실행되고 더이상 할것이 없을떄 되돌아감.
    else:
        bit[k] = 0
        subset(k+1)
        bit[k] = 1
        subset(k+1)
subset(0)

# # 바이너리카운팅을 이용한 부분집합
# arr = [-1,3,-9,6,7,-6,1,5,4,-2]
# # arr = [32,23,54,65]
# n = len(arr)
# for i in range(0,(1<<n)):	# 1<<n : 부분집합의 개수
#     tr = []
#     for j in range(0,n):	# 원소의 수만큼 비트를 비교함
#         # print("i값:" , i)
#         if i & (i << j):	# i의 j번째 비트가 1이면 j번째원소출력
#             tr.append(arr[j])
#             # print("{}".format(arr[j]), end = "")
#     if sum(tr) == 0:
#         print(tr)
#     print()

