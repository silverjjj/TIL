'''
우선순위 큐는 우선순위가 가장 높은 자료를 먼저 꺼내는 자료구조
python 에서는 heapq를 import하여 사용한다.
heapq구조는 기본적으로 min-heap
push의 순서와 상관없이 pop할땐 우선순위의 숫자가 가장 작은것부터 pop 시킨다.
push : heapq.heappush(리스트, (우선순위, 데이터))
pop : heapq.heappop(h)
'''

import heapq
h = []

heapq.heappush(h, (3, "Go to home"))
heapq.heappush(h, (10, "Do not study"))
heapq.heappush(h, (1, "Enjoy!"))
heapq.heappush(h, (4, "Eat!"))
heapq.heappush(h, (7, "Pray!"))
first = heapq.heappop(h)
second = heapq.heappop(h)
third = heapq.heappop(h)
print("first:", first)      # 1
print("second:", second)    # 3
print("third:", third)      # 4