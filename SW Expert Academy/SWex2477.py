'''
2 2 6 1 2
3 2
4 2
0 0 1 2 3 4
'''
N,M,K,A,B = map(int, input().split()) # 접수창고갯수,정비창고갯수,사람수, 지갑을 분실한 접수창고, 정비창고
a = list(map(int,input().split()))  # 접수창고 걸리는 시간
b = list(map(int,input().split()))  # 정비창고 걸리는 시간
time = [0] + list(map(int,input().split()))
arr = [[] for _ in range(0,K+1)]
print(arr)
receipt = [0] * N
repair = [0] * M

for num in range(1,len(time)):
    for i in range(N):
        if receipt[i] == 0:
            receipt[i] = 1
            print(num)
            arr[num].append(i)
            break

    for j in range(N):
        if receipt[j] == 0:
            break
        else:
            receipt[j] +=1
            if receipt[j] == a[j]:
                receipt[j] = 0
                break
print(arr)