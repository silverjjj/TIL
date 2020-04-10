#SWex4530
a,b = map(int,input().split())
a = abs(a)
def find(n):
    cnt = 0
    for i in range(1,n+1):
        num = str(i)
        for j in num:
            if j == "4":
                cnt += 1
                break
        if i>=4 and i % 4 == 0:
            cnt +=1
    return cnt

sum = find(a) + find(b)
print(find(a),find(b))
result = a+b -1 -sum
print(result)