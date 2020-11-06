'''
맨 앞자리에서 k+1의 값을 비교
가장 큰값의 idx의 앞에 있는 모든걸 지워버림 만약 앞에 n개라면 k -= n이됨
k = 0 될때까지 진행
'''
def solution(number, k):
    answer = ''
    arr = [int(number[0])]
    for num in number[1:]:
        num = int(num)
        while len(arr) > 0 and arr[-1] < num and k > 0:
            k -= 1
            arr.pop()
        arr.append(num)
    if k != 0:
        arr = arr[:-k]
    for num in arr:
        answer += str(num)
    # print(answer)
    return answer

number = "19999912"
k = 3
solution(number, k)