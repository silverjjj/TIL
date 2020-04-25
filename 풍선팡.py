def per(array, N):
    if len(array) == N:
        temp = [0] * N
        for i in range(N):
            temp[i] = array[i]
        drop(temp)
        return
    for i in range(W):
        array.append(i)
        per(array, N)
        array.pop()