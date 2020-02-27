def password(case):
    for i in range(len(case)-1):
        if case[i] == case[i+1]:
            case.pop(i)
            case.pop(i)
            return password(case)
    return

for tc in range(1,11):
    N, C = list(map(str, input().split(" ")))
    case = []
    for i in C:
        case.append(i)
    password(case)
    case = "".join(case)
    print("#{} {}".format(tc,case))