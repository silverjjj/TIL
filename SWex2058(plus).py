
num = input()
result = []
for i in range(0,len(num)):
    if 1 <= int(num) <= 9999:
        result.append(int(num[i]))
    else:
        print('1<=num<=9999의 범위가 아닙니다.')
        break

print(sum(result))