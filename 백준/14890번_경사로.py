def find(rm,l):
    global n
    cnt = 0
    for i in range(n):
        s = []
        # visit = [0] * (n-1)
        for j in range(n-1):
            s.append(rm[i][j] - rm[i][j+1])
        print(s)
        # if s == [0]*(n-1):
        #     cnt +=1
        # else:
        #     for k in range(n-1):
        #         if s[k] == 1:
        #             if 0<=k+l-1 < n-1:  # 범위내일때만
        #                 if s[k:l] == [0]*l-1 and visit[k:l] == 0:
        #                     visit[k:l] = 1
        #                     continue
        #                 else:
        #                     break
        #         elif s[k] == -1:
        #             if 0<=k-l+1 < n-1:
        #                 if s[k-l:k] == [0]* l-1 and visit[k-1:k] == 0:
        #                     visit[k-1:k] = 1
        #                     continue
        #                 else:
        #                     break


    return cnt

n,l = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]


print(find(rm,l))
