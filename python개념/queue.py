# def enq(n):
#     global rear
#     if rear == len(q) -1:
#         print('full')
#     else:
#         rear +=1
#         q[rear] = n
#
# q =[0]*3
# front = -1
# rear = -1


# 마이쮸문제
#
# n = 20 # 마이쮸개수
# q = [[1,0]] # 1번이 줄을 서고 아직 받지 않은 상태
# j = 1 # 새롭게 줄을 서는 사람 번호
# last = 0
# while n > 0:
#     i,m = q.pop(0)
#     m += 1 # 이번에 받을 개수
#     n-=m # 남은 마이쮸 개수
#     j += 1 # 새로 줄서는 사람의 번호
#     q.append([i,m]) # 맨 앞사람이 m개를 받아서 줄을섬
#     q.append([j,0]) # 새로 줄서는 사람. 아직 0개
#     last = i
#     print(i,m,n,q)
# print(last)

import queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())
