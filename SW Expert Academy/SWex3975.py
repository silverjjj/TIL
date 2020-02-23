# 이문제는 print출력보다 list에 값을 넣어 하나하나 빼는게 더 시간절약이 되는걸 알려준문제
'''
3
1 2 2 4
4 5 2 5
1 9 5 6
'''
T = int(input())
result = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    if B/A > D/C:
        ans = 'BOB'
    elif B/A == D/C:
        ans = 'DRAW'
    else:
        ans = 'ALICE'
    result.append(ans)
for i in range(0, T):
    print(f'#{i+1} {result[i]}')
