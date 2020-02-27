def f(i,N,K):   #i번째 원소를 포함하는 경우/ 아닌경우 -> 재귀호출
    global bit
    global cnt
    if i == N:      # base case : bit배열의 모든칸이 결정됨
        print(bit)
        s = 0       # sum
        for j in range(N):
            if bit[j] == 1:
                s += j+1    #선택된 원소의 누적값
        if s == K:      # 누적합이 K=10 과 같다면 카운팅함.
            cnt+=1
        return
    else:
        print(bit)
        bit[i] = 1        # i 번째 원소 선택된경우
        f(i + 1, N, K)
        bit[i] = 0          # i 번째 원소 선택 안된경우
        f(i + 1, N, K)

N = 10      # 원소수
K = 15     # 부분집합의 합
bit = [0]*N # 원소의 포함여부 저장
cnt = 0         # 조건을 만족하는 부분집합의 갯수
f(0,N,K)    # 부분집합을 구하고 -> 총합이 10인 부분집합갯수 세기
            #  N은 원소수, K는 부분집합의 합 EX.(1,2,8) 같은거
print(cnt)