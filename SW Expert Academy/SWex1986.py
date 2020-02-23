T = int(input())
count = 0
for N in range(1,T+1):
    N = int(input())
    if 1 <= N <= 10:
        sum1,sum2=0,0
        count += 1
        for j in range(1,N+1):
            if j % 2 == 1:
                sum1 += j
            elif j % 2 == 0:
                sum2 -= j
        print(f"#{count}",sum1+sum2)



# for i in len(num_list):
#     sum1,sum2=0,0
#     for j in range(1,T+1):
#         if j % 2 ==1:
#             sum1 +=j
#         elif j % 2==0:
#             sum2 -=j
#     print(sum1+sum2)
