s = []
for _ in range(1,1+int(input())):
    N, R = list(map(int, input().split()))
    a = b = 1
    result = 0
    for i in range(R):
        a *= N-i
        b *= R-i
    result = int(a/b) % (1234567891)
    s.append(result)
tc = 0

for i in s:
    tc +=1
    print("#{} {}".format(tc,i))