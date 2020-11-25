import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
for i in range(1,N):
    sum1 = arr[i] + arr[i-1]
    arr[i] = max(sum1, arr[i])
print(max(arr))