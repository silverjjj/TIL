#
def password(case):
    for i in range(len(case)-1):
        if case[i] == case[i+1]:
            case.remove(case[i])
            case.remove(case[i])
            return password(case)
    return case

N, C = list(map(str, input().split(" ")))
case = []
for i in C:
    case.append(i)
print(case[4])
a = password(case)
print(a)