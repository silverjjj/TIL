class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 삽입하기 : 배열의 마지막에 삽입 (완전 이진트리의 맨 마지막에 넣는다.)
    # 힙구조를 만들어줌
    def insert(self,k):  #self는 자기자신
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)   # 새롭게 추가위치가 어디서 만들어지는데 알기위해

    # 현재노드가 부모노드보다 작으면 자리변경 -> root까지 반복
    def percUp(self,i):
        # 나와 부모를 비교하는것
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i // 2]= self.heapList[i//2],self.heapList[i]
            i = i // 2

    def printHeap(self):
        print(self.heapList)

    # 삭제
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -=1
        self.heapList.pop()
        self.percDown(1)
        return retval

    # 자식들중 최소값의 위치찾기
    def minChild(self,i):
        # 자식중 한개밖에 없으면
        if i*2 +1 > self.currentSize:
            return i*2  # 왼쪽자식 리턴
        else:
            # 왼쪽자식 < 오른쪽 자식이면
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2  # 더 최소인 작은 왼쪽자식을 리턴
            else:
                return i*2+1

    def percDown(self,i):
        while i+2 <=self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = mc

hp = BinHeap()
arr = [34,27,3,50,40]
for n in arr:
    hp.insert(n)
    hp.printHeap()

# print(hp.delMin())
hp.delMin()

import heapq

# heapify
test = [1,3,2,6,8,0,6]
heapq.heapify(test)
print(test)
# heapq : push의 순서와 상관없이 Min - priority - queue 구조를 갖는다.
heapq.heappush(test, 3)
heapq.heappush(test, 5)
heapq.heappush(test, 1)
heapq.heappush(test, -3)
print(test)
print(heapq.heappop(test))