import sys
input = sys.stdin.readline

def rotate(tmp):
    for num, d in tmp:
        if d == -1:
            tmp = arr[num].pop(0)
            arr[num].append(tmp)
        elif d == 1:
            tmp = arr[num].pop(-1)
            arr[num].insert(0,tmp)

def simulation(num,d):
    if visited[num]:
        return
    visited[num] = 1
    tmp.append([num,d])
    if 0<=num+1<=3 and arr[num][2] != arr[num+1][6]:
        simulation(num+1, -d)
    if 0<= num-1 <= 3 and arr[num][6] != arr[num-1][2]:
        simulation(num-1, -d)

arr = [list(map(int,input())) for _ in range(4)]
n = int(input())
for _ in range(n):
    number, d = map(int,input().split())
    visited = [0]*4
    tmp = []
    simulation(number-1,d)
    rotate(tmp)
res = 0
for i in range(4):
    if arr[i][0] == 1:
        res += (2**i)
print(res)