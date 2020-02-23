# 문자열 슬라이싱
T = int(input())

for test_case in range(T):
    mun = input()
    for i in range(1,31):
        if mun[:i] == mun[i:i*2]:   #[:i] i포함x  [i:] i포함
            print(f'#{test_case+1} {i}')
            break

