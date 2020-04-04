# 이거 너무어려웠다..
def solution(numbers):
    result = []
    for number in numbers:
        origin = str(number)
        # print(origin[0])
        num = list(str(number))
        st = 0
        # print(origin)
        while len(num) <= 4:
            num.append(origin[st])
            st = (st + 1) % len(origin)
        num = int("".join(num))
        result.append([num,origin])
    # print(result)
    result = sorted(result,reverse = True)
    # print(result)
    return str(int("".join([item[1] for item in result])))
numbers = [121,12]
print(solution(numbers))