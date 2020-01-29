for test_case in range(1,int(input())+1):
    A,B,C,D = map(int,input().split())
    hr = A + C
    min = B + D
    if min >= 60:
        hr +=1
        min -=60
    if hr >= 13:
        hr -= 12
    print(f'#{test_case} {hr} {min}')