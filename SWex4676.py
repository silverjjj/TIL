T = int(input())
for tc in range(1, T+1):
    N = list(map(str,input()))
    num = int(input())          #하이푼 넣을 갯수
    h_position = list(map(int, input().split())) # 하이푼 넣을 위치
    h_position.sort()
    h_position.reverse()
    h = '-'
    new = []
    for i in h_position:
        N.insert(i,h)
    result = ''.join(N)
    print("#{} {}".format(tc,result))