'''
정렬
'''
arr = [4,33,76,28,8,9,23,1,90]
# 삽입정렬(Insert Sort)(O^2의 시간복잡도)

# N = len(arr)
# for i in range(1,N):
#     tmp = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] > tmp:
#         arr[j+1] = arr[j]
#         j -=1
#     arr[j+1] = tmp
# print(arr)

# 병합정렬(시간복잡도 :nlogn) 가장 효율적인 방식
