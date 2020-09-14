

def simulation(arr,num,d):
    print("============================")
    s = [[num,d]]
    visited = [0] * 4
    while s:
        print(s)
        num,d = s.pop()
        # 방문표시
        if visited[num]:
            continue
        visited[num] = 1
        if num == 0:
            if arr[num][2] != arr[num + 1][-2]:
                s.append([num+1,-d])
        elif num == 3:
            if arr[num][2] != arr[num - 1][-2]:
                s.append([num-1,-d])
        else:
            if arr[num][2] != arr[num - 1][-2]:
                s.append([num-1,-d])
            if arr[num][2] != arr[num + 1][-2]:
                s.append([num+1,-d])

        if d == -1:
            char = arr[num]
            first = char.pop(0)
            arr[num].append(first)
        elif d == 1:
            char = arr[num]
            last = char.pop()
            arr[num].insert(0,last)
    return arr
arr = []
for _ in range(4):
    char= list(str(input()))
    arr.append(char)
n = int(input())
for _ in range(n):
    num, d = map(int,input().split())
    arr = simulation(arr,num-1,d)
res = 0
for i in range(4):
    if arr[i][0] == '1':
        res += (2**i)
print(res)