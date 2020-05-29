# 문제1 스도쿠게임
def find(x,y,num):
    # nx,ny는 3*3크기의 격자의 맨왼쪽 맨위의 좌표
    nx = (x // 3)*3
    ny = (y // 3)*3
    # 3*3배열에서 해당 번호 num이 있으면 False로 바로 리턴
    for i in range(3):
        for j in range(3):
            if Sudoku[nx + i][ny + j] == num:
                 return False
    # 열에서 num을 찾으면 바로 False로 리턴
    for k in range(9):
        if Sudoku[k][y] == num:
            return False
    # 행에서 num이 없어야 True 리턴하는 if문
    if num not in Sudoku[x][:]:
        return True
    else:
        return False

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    # 스도쿠 배열
    Sudoku = [list(map(int,input().split())) for _ in range(9)]
    # nums : 행번호, 열번호, 숫자를 담을 배열
    nums = []
    for i in range(n):
        arr = list(map(int,input().split()))
        nums.append(arr)
    cnt = 0
    # nums에서 한배열씩 함수로 간다.
    for number in nums:
        x, y, num = number[0],number[1],number[2]
        # 해당 함수가 True로 리턴을 해야만 행,열,3*3에 해당 num이 없음을 알고 cnt+=1을 해준다.
        if find(x,y,num) == True:
            cnt +=1
        else:   # 만약 True가 아니라면 바로 for문을 나가기 위한 break
            break
    print("#{} {}".format(tc,cnt))