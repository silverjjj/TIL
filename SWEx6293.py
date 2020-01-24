'''
다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
'''
from math import pi
num = input()
num_list = list(map(int,num.split(",")))

result = ""
for i in num_list:
    result += "%0.2f, " % (2 * pi * i)

print(result[0:-2])