import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(str,input().split())) for _ in range(N)]
arr.sort(key= lambda x:[-int(x[1]),int(x[2]),-int(x[3]),x[0]])
for ans in arr:
    print(ans[0])

'''

12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 90
nsj 70 70 90
Taewhan 50 60 90

'''