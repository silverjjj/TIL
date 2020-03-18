def f(i,n):
    if i == n:
        return
    else:
        print(i, '안녕 !!')
        f(i+1,n)
        print(i, ' 안녕 !!')

f(0,3)