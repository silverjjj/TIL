for tc in range(1, 1+int(input())):
    s = input()
    N = len(s)
    ans = "Not exist"
    if N ==1:
        ans = "Exist"
    else:
        i = 0
        while i < N//2 and (s[i] ==s[N-1-i] or s[i] =="?" or s[N-1-i]=="?"):
            i+=1
        if i == N//2:
            ans ="Exist"
    print("#{} {}".format(tc,ans))