'''
순열을 통해 구하려고했으나 시간초과가 났음.
특히 dfs를 사용을 전혀 생각하지 못함. 난 dfs를 쓸때 반복문 사용에 익숙해져있어서 더욱 그랬던것 같음.
dfs의 함수구현에 대해 다시한번 생각해보는 문제였음.
'''

def dfs(idx,sum):
    global maxV, minV
    if idx == n-1:
        if sum > maxV:
            maxV = sum
        if minV > sum:
            minV = sum
        return

    for j in range(4):
        if math[j] > 0:
            math[j]-=1
            if j == 0:
                result = sum + arr[idx+1]
            elif j == 1:
                result = sum - arr[idx+1]
            elif j == 2:
                result = sum * arr[idx+1]
            elif j == 3:
                result = int(sum / arr[idx+1])
            dfs(idx+1, result)
            math[j]+=1

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    math = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    maxV = -100000000
    minV = 100000000
    dfs(0,arr[0])
    print("#{} {}".format(tc,maxV-minV))

'''
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6
'''