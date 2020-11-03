N = int(input())
nums = list(map(int,input().split()))
maxV = max(nums)
weight = [0] * (maxV + 1)
dist = [0] * (maxV + 1)

for num in nums:
    maxC = max(weight[:num])
    weight[num] = maxC + 1
    tmp = 0
    for i in range(num):
        if weight[i] == maxC:
            tmp = i
    dist[num] = num + dist[tmp]
maxN = weight.index(max(weight))
print(dist[maxN])
'''

5
10 90 20 80 100
210

8
3 10 2 7 11 5 13 8
37

'''