T = int(input())
for i in range(1,T+1):
    num1, num2 = map(int, input().split())
    if (0 <= num1<= 10000) and (0 <= num2 <= 10000):
        print(f"#{i}",end = " ")
        if num1 > num2:
            print(">")
        elif num1 == num2:
            print("=")
        elif num1 < num2:
            print('<')
    else:
        0