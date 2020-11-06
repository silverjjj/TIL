# 최소힙만 지원
'''
힙은 해당 힙배열에 푸쉬할때마다 2진배열로 나열이 된다.
이 배열을 pop할경우 작은값부터 pop된다.
'''
print("최소힙지원")
import heapq
tmp = [7,2,5,3,4,6]
heap = []
for h in tmp:
    heapq.heappush(heap,h)
print(heap)
heapq.heappush(heap,1)
print(heap)
while heap:
    print(heapq.heappop(heap), end=" ")
print()
# 최대힙 지원
print("최대힙 지원")
tmp = [7,2,5,3,4,6]
heap = []
for h in tmp:
    heapq.heappush(heap,-h)
print(heap)
heapq.heappush(heap,-1)
print(heap)
while heap:
    tmpV = heapq.heappop(heap)
    print(-tmpV, end=" ")
