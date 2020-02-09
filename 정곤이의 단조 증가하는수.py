T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    print(len(arr[0]))

    for j in range(15):
        for i in range(5):
            if i < len(arr[i]):
                result = "".join(arr[i][j])
                print(result, end ="")