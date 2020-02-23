T = int(input())

for tc in range(1,T+1):

    N = int(input())
    numbers = list(map(int,input().split()))
    a = []
    # numbers중에서 맨앞 뒤가 될수있는 갯수 1개인 수를 뽑아낸다.
    for i in numbers:
        if numbers.count(i)%2 ==1:
            a.append(i)
    # 자리가 0인 맨앞 or 홀수인 맨뒤를 알수도록 index를 활용
    if numbers.index(a[0]) % 2 == 0:
        start = numbers.index(a[0])
    else:
        start = numbers.index(a[1])

    result = []
    result.append(numbers[start])
    result.append(numbers[start+1])

    # 새로운 리스트인 result에 짝에맞게 넣는다.
    while len(result) != len(numbers):
        for i in range(0,len(numbers),2):
            if result[-1] == numbers[i]:
                result.append(numbers[i])
                result.append(numbers[i + 1])
    result = ' '.join(list(map(str,result)))
    print(f'#{tc} {result}')