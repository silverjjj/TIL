def food_sum(tmp,m,k):
    global total
    if k == 0:
        x = food[0]
        y = food[1]
        total += (rm[x][y]+rm[y][x])
    elif m < k:
        return
    else:
        food[k-1] = tmp[m-1]
        # 1 tr이 꽉찰때까지
        food_sum(tmp,m-1,k-1)
        food_sum(tmp,m-1,k)
    return total

# 하나의 배열을 2개로 나눠 조합을 만드는함수
def comb(k,a,b):
    global minV,total
    if k == n and len(A) == len(B):
        total = 0
        food_sum(A, len(A), 2)
        tmp = total
        total = 0
        food_sum(B, len(B), 2)
        result = abs(tmp - total)
        if minV > result:
            minV = result
    elif k >= n:
        return
    else:
        if a < n//2:
            A.append(arr[k])
            comb(k+1,a+1,b)
            A.pop()
        if b < n//2:
            B.append(arr[k])
            comb(k+1,a,b+1)
            B.pop()
    return minV

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [list(map(int,input().split())) for _ in range(n)]
    arr = [num for num in range(n)]
    A = []
    B = []
    total = 0
    minV = 1234567
    food = [0]*2
    print("#{} {}".format(tc,comb(0,0,0)))

'''
3
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
4
0 7 1 1
7 0 6 2
1 1 0 2
10 1 9 0
6
0 37 26 52 77 20
32 0 15 26 75 16
54 33 0 79 37 90
92 10 66 0 92 3
64 7 89 89 0 21
80 49 94 68 5 0
'''


# def comb(n,a,b):
#     if n == N and len(A) == len(B):
#         return
#     elif n >= len(arr):
#         return
#     else:
#         if a < N//2:
#             A.append(arr[n])
#             comb(n+1,a+1,b)
#             A.pop()
#         if b < N//2:
#             B.append(arr[n])
#             comb(n+1,a,b)
#             B.pop()
#
# arr = [0,1,2,3]
# A = []
# B = []
# N = len(arr)
# comb(0,0,0)