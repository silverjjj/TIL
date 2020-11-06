#SWex4828 min max
for tc in range(1,1+int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    maxV = minV = arr[0]
    for i in range(n):
        if arr[i] >= maxV:
            maxV = arr[i]
        elif arr[i] < minV:
            minV = arr[i]
    print("#{} {}".format(tc,maxV - minV))