def perm(n):
    global cnt
    if p[0] == 1:
        # print(p)
        if n == k:
            cnt += 1
            # if cnt % 2 == 1:
            #     # print(p,cnt)
        else:
            for i in range(k):
                if not used[i]:
                    used[i] = 1
                    p[n] = arr[i]
                    perm(n+1)
                    used[i] = 0
    else:
        return

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
k = len(arr)
used = [0]*k
p = [1]+[0]*(k-1)
cnt = 0
perm(0)