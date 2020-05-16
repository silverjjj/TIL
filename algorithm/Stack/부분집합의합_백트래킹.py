def f(i,N,K,s,r):
    # i:원소의 위치, N : 집합의 원소 K: 내가 원하는 부분집합의 합 s :sum ,r
    global cnt
    #base case :
    if s == K :     # 만약 원소들의 합이 10 이면,
        cnt +=1     # 카운팅을 해준다.
        return
    elif i == N:        #모든원소를 고려했는데 합이 K되는게 없을경우
        return
    elif s > K:         # 현재까지의 누적합이 K보다 크면 더 탐색할 필요없음.
        return
    elif s + r < K:        # 현재까지의합 + 후보군의 합이 K보다 작으면 정답이될 확률이 X
        return
    else:
        # i번째 요소가 선택된 경우
        f(i+1, N, K, s+i+1, r-(i+1))      #s+i+1 i 가 0부터 시작해서 +1을 해준다.
        # i번째 요소가 선택되지 않은 경우
        f(i+1, N, K, s, r-(i+1))
        # 재귀호출


N = 20  # 1부터 20까지가 집합의 원소
K = 10  # 부분집합의 합
cnt = 0
bit = [0]*N

f(0, N, K, 0, (1+N)*N//2)   #원소의 위치(i) 부분집합의 합, 선택후보들의 합
print(cnt)