'''
BOJ 10610

30의 배수가 되는 가장 큰수
N은 100000개의 숫자까지 가능

0이 무조건 존재해야함
3의 배수란 말은
총합이 3의 배수
'''
N = list(map(int,input().rstrip()))
if 0 in N:
    if sum(N) % 3 == 0:
        N.sort(reverse=True)
        for i in N:
            print(str(i),end="")
    else:
        print("-1")
else:
    print("-1")