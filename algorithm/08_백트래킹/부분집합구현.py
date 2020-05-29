# [1,2,3,4,5,6,7,8,9,10]의 powerset중 원소의 합이 10인 부분집합을 모두 출력하라
# # 내가푼 알고리즘
def subset(k,sum_num):
    global cnt
    cnt +=1
    if sum_num > 10:    # 가지치기
        return
    if k == n:          # 목표도달
        if sum_num == 10:
            for i in range(n):
                if visited[i]:
                    print(arr[i], end=" ")
            print()
        return
    else:
        visited[k] = 1
        subset(k+1,sum_num+arr[k])
        visited[k] = 0
        subset(k+1,sum_num)

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
cnt = 0
visited = [0]* n
subset(0,0)
print("내가푼것",cnt) # 2000번 -> 400번으로 줄임,, 함수에서 계속해서 sum을 해주자

# def backtrack(arr, idx, n, selected,sum_num):
#     global cnt
#     cnt +=1
#     if sum_num > 10:        # 가지치기
#         return
#     if idx == n:            #목표도달
#         if sum_num == 10:
#             for i in range(n):
#                 if selected[i]:
#                     print(arr[i], end = " ")
#             print()
#         # 총합이 10일때 출력
#         return
#     selected[idx] = 1       # visited임
#     # sum_num +=arr[idx]
#     backtrack(arr, idx+1, n, selected, sum_num + arr[idx])
#
#     selected[idx] = 0
#     # sum_num -= arr[idx]
#     backtrack(arr, idx + 1, n, selected, sum_num)
#
# arr = [1,2,3,4,5,6,7,8,9,10]
# cnt = 0
# backtrack(arr, 0, len(arr), [0]*10, 0)
# print("강의",cnt) # 400번
#
