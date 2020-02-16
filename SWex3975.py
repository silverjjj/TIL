for tc in range(1, int(input())+1):
    A, B, C, D = map(int, input().split())
    ans = 'ALICE'
    if A/B < C/D:
        ans = 'BOB'
    elif A/B == C/D:
        ans = 'DRAW'
    print(f'#{tc} {ans}')
