import sys
input = sys.stdin.readline

N = int(input())
dict = {}
for _ in range(N):
    age,name = map(str,input().split())
    age = int(age)
    if age in dict.keys():
        dict[age].append(name)
    else:
        dict[age] = [name]
nums = list(dict.keys())
nums.sort()
for num in nums:
    for val in dict[num]:
        print(num, val)