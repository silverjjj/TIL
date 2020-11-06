N = int(input())
arr = []
for i in range(N):
    put = input().split()
    arr.append(put[0]*int(put[1]))

for i in range(len(arr)):
    print(arr[i],end = "")

