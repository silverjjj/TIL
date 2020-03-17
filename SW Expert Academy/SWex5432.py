# SWex5432 쇠막대기 자르기
# 문제를 수학적으로 풀고 이를 코딩으로 구현하는것이 중요.. 순서를 잘보자
for tc in range(int(input())):
    case = str(input())
    n = len(case)
    print(case[0])
    stick = 0
    cnt = 0
    for i in range(n):
        if case[i] == "(":
            stick +=1
        elif case[i] == ")":
            stick -=1
            if case[i-1] == "(":
                cnt += stick
            elif case[i-1] ==")":
                cnt +=1
    print("#{} {}".format(tc+1,cnt))