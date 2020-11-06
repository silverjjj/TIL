# 문자열에서 문자개수를 세는 count함수

N = int(input())
for i in range(1,N+1):
    house = str(i)

    count = house.count('3') + house.count('6')+house.count('9')
    if count:
        print('-'*count, end = " ")
    else:
        print(house, end = " ")

