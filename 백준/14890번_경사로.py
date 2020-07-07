def stair(arr):
    now_val = arr[0]
    visited = [0]*N
    for idx, val in enumerate(arr):
        # 현재층과 다음층이 같을경우
        if now_val == val:
            continue
        # 현재층과 다음층의 차이ㅏ 2이상일경우 바로 false
        elif abs(now_val - val) >= 2:
            return False

        # 현재에서 다음층으로 올라갈경우
        elif (now_val - val) == -1:
            # val의 idx를 기준으로 왼쪽 L개가 같아야함 그리고 L개 모두 사용안한자리
            for i in range(idx -1 , idx - L -1, -1):
                if 0 <= i < N and visited[i] == 0 and now_val == arr[i]:
                    visited[i] = 1
                else:
                    return False
        # 현재에서 다음층으로 내려갈경우
        elif (now_val - val) == 1:
            # val의 idx를 포함하여 오른쪽 L개가 같아야함 그리고 L개 모두 사용안한자리
            for i in range(idx, idx + L):
                # print(now_val)
                if 0 <= i < N and visited[i] == 0 and now_val-1 == arr[i]:
                    visited[i] = 1
                else:
                    return False

        # 한턴을 넘기면 현재의 값을 갱신
        now_val = val
    return True

N,L = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
# 행
for row in mapping:
    if stair(row):
        cnt +=1
# 열
for j in range(N):
    col = [row[j] for row in mapping]
    if stair(col):
        cnt +=1
print(cnt)