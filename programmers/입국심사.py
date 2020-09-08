'''
사람 n 명
심사관 times 배열인원


'''

def solution(n, times):
    arr = []
    times.sort()
    cnt = 0
    while True:
        cnt += 1
        for time in times:
            if cnt % time == 0:
                arr.append(cnt)
        if len(arr) >= n:
            break
    print(arr)
    return arr[n-1]
n = 6
times = [10,7]
print(solution(n, times))