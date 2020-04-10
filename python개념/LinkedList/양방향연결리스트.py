class Node:
    def __init__(self,d=0,p=None, n = None):
        self.data = d
        self.prev = p
        self.next = n
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addLast(lst,arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val,last)
        last.next = new # last의 next는 new로 된다
        last = new

    if lst.head is None: #빈리스트인경우
        lst.head, lst.tail = first,last
    else:   # 빈리스트가 아닌경우
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None:
            # 마지막
            first.prev = lst.tail
            lst.tail.next = first    # tail의 next를 firt랑 연결
            lst.tail = last         # tail을 맨 마지막인 last로 이동
        elif cur.prev is None:
            #처음
            last.next = lst.head
            lst.head.prev = last  # a맨처음의 prev를 last로
            lst.head =first
        else:    # 중간
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
        lst.size += len(arr)

    # if lst.head is None:
    #     lst.head = lst.tail = new
    # else:
    #     new.prev = lst.tail
    #     lst.tail.next = new
    #     lst.tail = new
    # lst.size+=1

def printList(lst):
    if lst.head is None: return
    cur = lst.head
    while cur is not None:
        print(cur.data , end = " ")
        cur = cur.next
    print()
    # 역방향
    cur = lst.tail
    while cur is not None:
        print(cur.data , end = " ")
        cur = cur.prev
    print()


mylist = LinkedList()
arr = [1,3,5,7,9]
# for val in arr:
addLast(mylist,arr)
printList(mylist)

addLast(mylist,[0,1,2])
printList(mylist)