'''
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
[제약 사항]
자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)
[입력]
입력으로 자연수 N이 주어진다.
[출력]
각 자릿수의 합을 출력한다.
'''
num = input()
result = []
for i in range(0,len(num)):
    if 1 <= int(num) <= 9999:
        result.append(int(num[i]))
    else:
        print('1<=num<=9999의 범위가 아닙니다.')
        break

print(sum(result))