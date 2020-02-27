for tc in range(1,11):
    N = int(input())
    origin = list(map(int,input().split()))
    C = int(input())
    case = list(map(str,input().split()))
    for i in range(len(case)):   # i = 0
        if case[i] == "I":
            for j in range(int(case[i+2])): # j = 0~5
                origin.insert(int(case[i+1])+j, int(case[i+3+j]))
        elif case[i] == "D":
            for j in range(int(case[i + 2])):  # j = 0~5
                origin.pop(int(case[i+1]))
        elif case[i] == "A":
            for j in range(int(case[i+1])):
                origin.append(int(case[i+2+j]))

    result = list(map(str,origin[0:10]))
    result = " ".join(result)
    print("#{} {}".format(tc,result))
