k = int(input())
arr = [list(map(int,input().split())) for _ in range(4)]
for row in arr:
    print(row)
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]
cnt = 0
while k > cnt:
    n, m = map(int, input().split())
    # i = 1,6이 만나면 돌려짐
    for i in range(0,3):
        if arr[i][2] == arr[i+1][6]:
            


