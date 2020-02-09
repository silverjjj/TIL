
for tc in range(1, int(input())+1):
    N = int(input())
    # 양의정수의합
    sum1 = sum2 = sum3 =0
    cnt1 = i = 0
    cnt2 = j = 0
    sum1 = N*(N+1)//2
    #홀수의합
    sum2 = N**(2)
    #짝수의합
    sum3 = sum1*2
    print("#{} {} {} {}".format(tc,str(sum1),str(sum2),str(sum3)))