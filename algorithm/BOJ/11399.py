N = int(input())
arr = list(map(int,input().split()))
tmp = 0
result = 0
arr.sort()
for num in arr:
    tmp += num
    result += tmp
print(result)