def find(m):
    for _ in range(m):
        en, *args = input().split()

        if en == "I":
            arr.insert(int(args[0]), int(args[1]))
        elif en == 'D':
            arr.pop(int(*args[0]))
        elif en == "C":
            arr.pop(int(args[0]))
            arr.insert(int(args[0]),int(args[1]))

T = int(input())
for tc in range(1,T+1):
    n,m,l = map(int,input().split())
    arr = list(map(int,input().split()))
    find(m)
    try:
        result = arr[l]
    except IndexError:
        result = -1
    print("#{} {}".format(tc,result))