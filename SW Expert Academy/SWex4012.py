# an[] : n개의 원소를 가지고있는 배열
# tr[] : r개의 크기의 배열, 조합이 임시 저장될 배열
def comb(n,r,arr):
    global total
    if r == 0:  # r-=1하면서 r ==0일때 출력
        # 2. tr꽉차면 출력
        print(tr)
        if tr not in total:
            print(tr)
            tmp = []
            for i in arr:
                tmp.append(i)
            for num in tr:
                if num in tmp:
                    tmp.remove(num)
            print(tmp)
            total.append(tmp)
            total.append(tr)
            print("------")
            print(total)
    elif n < r:			# 4C5같은게 있을수도 있으니,, 에러를 빼주는거
        return
    else:
        # print(n-1,r-1)
        tr[r-1] = arr[n-1]	# 마지막데이터(an[n-1])을 넣어주고
        # 1. tr이 꽉찰때까지
        comb(n-1,r-1,arr)		# 마지막데이터가 있는경우
        # 3. return 되서 여기로
        comb(n-1,r,arr)			# 마지막데이터가 없는경우

arr = [0,1,2,3,4,5,6,7]
n = len(arr)
r = 4
tr = [0]*r      # 결과를 담는배열
total = []
comb(n,r,arr)   # 5,3에서 시작