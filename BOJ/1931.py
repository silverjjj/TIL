import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x,y = map(int,input().split())
    arr.append([x,y])
arr.sort(key = lambda x : (x[1], x[0]))
cnt = 0
cur_end = 0
for next_st, next_end in arr:
    if next_st >= cur_end:
        cur_end = next_end
        cnt += 1
print(cnt)