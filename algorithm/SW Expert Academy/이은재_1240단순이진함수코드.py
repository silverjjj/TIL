# SWex1240 [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

def find(arr):
    global arr_one
    for i in range(n):
        # 오른쪽 위에부터 시작하자
        for j in range(m - 1, -1, -1):
            if arr[i][j] == '1':
                arr_one = arr[i][j - 55:j+1]
                return arr_one
T = int(input())
for tc in range(1,T+1):
    n, m = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(n)]
    # nums들의 특징은 맨 뒷자리가 모두 1이기 때문에 이걸 이용해보자
    nums = ['0001101','0011001', '0010011', '0111101', '0100011',
             '0110001', '0101111', '0111011', '0110111', '0001011']
    arr_one = []
    # arr가 다 필요없구 한 줄만필요하기 때문에 한줄만 빼오자
    find(arr)
    # 총 56개의 숫자가 나오면 7개씩 나눠서 새로운 new_arr배열에 집어넣자
    new_arr = []
    for i in range(0,56,7):
        num="".join(arr_one[i:i + 7])
        new_arr.append(num)
    r = []
    for i in new_arr:
        for j in range(len(nums)):
            if i == nums[j]:
                r.append(j)

    code_sum = (r[0]+r[2]+r[4]+r[6])*3 +(r[1]+r[3]+r[5]+r[7])
    if code_sum % 10 == 0:
        result = sum(r)
    else:
        result = 0
    print("#{} {}".format(tc, result))