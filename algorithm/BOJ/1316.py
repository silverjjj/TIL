'''
BOJ1316
'''
def find_group(char):
    L = len(char)
    cnt = 0
    dist = {}
    while L > cnt:
        cur = char[cnt]
        if dist.get(cur):
            return False
        else:
            dist[cur] = 1
            while (cnt == L-1) or (L > cnt and cur == char[cnt+1]):
                cnt += 1
            cnt += 1
    return True

N = int(input())
res = 0
for _ in range(N):
    char = str(input())
    if find_group(char):
        res += 1
print(res)