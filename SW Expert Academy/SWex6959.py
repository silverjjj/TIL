# SWex6959 이상한 나라의 덧셈게임
T = int(input())
for tc in range(1,T+1):
    num = list(map(str,input()))
    # print(num)
    sum = cnt = 0
    while len(num) != 1:
        for i in range(len(num),1,-1):
            a = int(num.pop())
            b = int(num.pop())
            # print(a,b,num)
            sum = a+b
            if sum > 9:
                x = sum // 10
                y = sum % 10
                num.append(str(x))
                num.append(str(y))
            else:
                num.append(str(sum))
            cnt +=1
    if cnt % 2 == 1:
        name = 'A'
    else:
        name = 'B'
    print("#{} {}".format(tc,name))