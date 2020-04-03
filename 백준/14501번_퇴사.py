def find(i,arr):
    global sum
    if i >= n:
        return sum
    s = []
    v = arr[i]
    s.append(v)
    t,p = s.pop()
    # print(t,p,i+t)
    if i+t <= n:
        sum += p
    print
    find(i+1, arr)

n = int(input())
arr = []
sum_list = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])
for i in range(n):
    sum = 0
    maxV = 0
    find(i,arr)
    sum_list.append(sum)
print(max(sum_list))