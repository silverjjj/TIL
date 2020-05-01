def Binary(num):
    global result, cnt
    while True:
        next_num = num * 2
        result += str(int(next_num))
        num = next_num - int(next_num)
        cnt += 1
        if num == 0.0:
            return
        if cnt > 13:
            return

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    result = ''
    cnt = 0
    Binary(num)
    if cnt > 13:
        print("#{}".format(tc)+' overflow')
    else:
        print("#{} {}".format(tc, result))