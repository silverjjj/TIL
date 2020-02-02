for tc in range(1,int(input())+1):
    sudoku = []
    total = []
    cnt = 0
    for i in range(9):
        n = list(map(int, input().split()))
        sudoku.append(n)

    for i in range(9):
        for j in range(9):
            total.append(sudoku[i][j])
            total.sort()
        if total == [1,2,3,4,5,6,7,8,9]:
            cnt += 1

        cnt += 0
        del total[0:9]


    for j in range(9):
        for i in range(9):
            total.append(sudoku[i][j])
            total.sort()
        if total == [1,2,3,4,5,6,7,8,9]:
            cnt += 1
        cnt += 0
        del total[0:9]

    for y in range(0,9,3):
        for x in range(0,9,3):
            for i in range(3):
                for j in range(3):
                    total.append(sudoku[i+x][j+y])
                    total.sort()
            if total == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                cnt += 1
            cnt += 0
            del total[0:9]

    if cnt == 27:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")

# for tc in range(1,int(input())+1):
#     sudoku = []
#     for i in range(9):
#         n = list(map(int, input().split()))
#         sudoku.append(n)
#
#     print(f"#{tc} {result}")