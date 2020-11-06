#SWex4408 자기방으로 돌아가기
for tc in range(1,int(input())+1):
    n = int(input())
    arr = [0]*200  # 0 ~ 199   (1~400)
    for i in range(n):
        x,y = map(int,input().split())
        if x > y:
            x, y = y, x
        x = (x -1)//2
        y = (y -1)//2
        for j in range(x,y+1):
            arr[j] +=1
    print("#{} {}".format(tc,max(arr)))