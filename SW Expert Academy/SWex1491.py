for tc in range(1,1+int(input())):
    n,a,b= list(map(int, input().split()))
    minV = 987654321
    sum =0
    n1 = int(n**0.5)
    for r in range(n1,n+1):
        for c in range(1,n1+1):
            if r * c <= n:
                sum = a*abs(r-c) + b*(n-(r*c))
                if sum < minV:
                    minV = sum

    print("#{} {}".format(tc,minV))


