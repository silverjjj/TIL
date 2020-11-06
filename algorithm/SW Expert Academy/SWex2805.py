T = int(input())
for tc in range(1,T+1):
    n = int(input())
    farm = [list(map(int,input())) for _ in range(n)]
    end = 1
    point = n-1
    sum = 0
    i = 0
    j = n//2
    while i < n//2:
        for tmp in range(j,j+end):
            sum += (farm[i][tmp]+farm[i+point][tmp])
        i+=1
        j-=1
        end +=2
        point -=2
    for y in range(n):
        sum +=farm[n//2][y]
    print("#{} {}".format(tc,sum))