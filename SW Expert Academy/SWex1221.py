T = int(input())
for tc in range(1,T+1):
    N = list(map(str,input().split()))
    case = list(map(str,input().split()))
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []
    for j in range(len(num)):
        for i in range(0,len(case)):
            if num[j] == case[i]:
                result.append(case[i])
    result = " ".join(result)
    print("#{}".format(tc))
    print(result)