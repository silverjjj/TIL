#SWex4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
for tc in range(int(input())):
    a = int(input())
    n = list(map(int,input().split()))
    n.sort()
    small = []
    big = []
    result = []
    for i in range(a//2):
        small.append(n[i])
        big.append(n[-1-i])
    for j in range(5):
        result.append(big[j])
        result.append(small[j])
    print(f"#{tc+1}", end = " ")
    for k in range(10):
        print(result[k], end = " ")
    print()