'''
A,B의 자카드 유사도
교 / 합

A와 B가 공집합일경우
교 / 합은 1로 정의

A
'''
eng = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    n1 = len(str1)
    n2 = len(str2)
    A = {}
    B = {}
    for i in range(n1-1):
        if str1[i] in eng and str1[i+1] in eng:
            if str1[i]+str1[i+1] in A.keys():
                A[str1[i] + str1[i + 1]] += 1
            else:
                A[str1[i]+str1[i+1]] = 1
    for i in range(n2-1):
        if str2[i] in eng and str2[i+1] in eng:
            if str2[i]+str2[i+1] in B.keys():
                B[str2[i] + str2[i + 1]] += 1
            else:
                B[str2[i]+str2[i+1]] = 1
    union = []
    inter = []
    for a_key, a_val in A.items():
        if a_key in B.keys():
            if a_val >= B[a_key]:
                maxV = a_val
                minV = B[a_key]
            else:
                minV= a_val
                maxV= B[a_key]
            for _ in range(maxV):
                union.append(a_key)
            for _ in range(minV):
                inter.append(a_key)
        else:
            for _ in range(a_val):
                union.append(a_key)
    for b_key, b_val in B.items():
        if b_key not in union:
            for _ in range(b_val):
                union.append(b_key)

    if len(inter) == 0 and len(union) == 0:
        return 65536
    res = (len(inter) / len(union)) * 65536
    return int(res)

str1 = 'FRANCE'
str2 = 'french'
solution(str1, str2)