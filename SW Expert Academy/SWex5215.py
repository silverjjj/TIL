#SWex5215
def gogo(idx,score,cal):
    global maxV,n,l
    global case
    # print(maxV)
    if idx == n:
        if cal <=l:
            if score > maxV:
                maxV = score
    elif cal > l:
        return
    else:
        s,c = case[idx]
        gogo(idx+1,score+s,cal+c)
        gogo(idx + 1, score, cal)

for tc in range(int(input())):
    n, l =map(int,input().split())
    case = []
    for _ in range(n):
        a,b = map(int,input().split())
        case.append([a,b])
    maxV = 0
    gogo(0,0,0) # idx, score, cal 이 0부터 시작
    print("#{} {}".format(tc+1,maxV))
