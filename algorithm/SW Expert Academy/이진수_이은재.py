T = int(input())
for tc in range(1,T+1):
    n, bit = input().split()
    # 계산하기 편하게 reversed를 한다.
    bit = list(reversed(bit))
    en = [['A','B','C','D','E','F'], [10,11,12,13,14,15]]
    # print(bit)
    remainder = []
    for num in bit:
        # 리스트를 이용하여 영어 -> 숫자변환
        if num in en[0]:
            for k in range(6):
                if num == en[0][k]:
                    num = en[1][k]

        # num을 int형으로 변환
        num = int(num)
        # 나머지를 remainder 리스트에 모아준다.
        for _ in range(4):
            remainder.append(num % 2)
            num = num // 2

    # 정답에 맞게 str로 바꾼디 join 시켜준다.
    result = []
    for i in remainder:
        result.insert(0,str(i))
    result = "".join(result)

    print("#{} {}".format(tc,result))