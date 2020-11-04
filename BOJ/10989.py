import sys
input = sys.stdin.readline
arr = [0] * 10001
N = int(input())
for _ in range(N):
    num = int(input())
    arr[num] = arr[num] + 1

for i in range(len(arr)):
    if arr[i] !=0:
        for _ in range(arr[i]):
            print(i)
