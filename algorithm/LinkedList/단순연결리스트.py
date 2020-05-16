class Node:
    def __init__(self, d=0, n=None):
        self.data = d       #데이터
        self.next = n       #다음 요소의 주소
    # Node(0,None)

class LinkedList:
    def __init__(self):
        self.head = None    #리스트의 처음
        self.tail = None
        self.size = 0       #리스트의 길이
# 여기 위까진 붕어빵의 틀같은거..
# 이제부턴 그 틀을 이용해 붕어빵을 만들어보자

mylist = LinkedList() # 연결 리스트 객체 생성 -> 객체의주소(메모리)를 mylist변수에 담음

# 출력하기
def printList(lst):
    # cur = lst.head
    # print(cur.data)
    # # cur = 100
    # # cur.next은 200임 이를 cur에 할당
    # cur = cur.next
    # print(cur.data)
    # cur = cur.next
    # print(cur.data)
    # cur = cur.next
    # print(cur.data)


# 각 노드를 생성
    cur = lst.head
    print(lst.size, '[', end = " ")
    while cur is not None:  # 결국 마지막자리의 next가 none이 나오니까 마지막까지 돌린다는말
        print(cur.data, end = " ")
        cur = cur.next
    print("]")

#리스트 마지막에 추가하기
def insertLast(lst, new):    # new는 메모리 주소
    '''
    맨 처음 lst.head는 none입니다. 그래서 첫 시작점으 잡아주기위해 node(0)의 주소인 new(100)에 할당해줍니다
    그런뒤 i = 1에서 다시 함수로 들어옵니다.
    lst.head = new(100) 기 때문에 else문으로 들어가 임의의 변수 cur(cur은 head와 next를 다 갖는 붕어빵 틀이라고 생각합시다.)에 list.head(new)를 할당합니다(붕어빵틀이 이동한거)
    그런뒤 while문의 cur.next가 none이 아닌값(다음 주소가 있는값 ex)200  ) 을찾으면 cur을 해당 주소로 이동합니다(cur = cur.next)
    이동한 cur의 next는 new(200)로 합니다 여기서 new는 메모리 주소

    위 과정을 반복
    '''
    # 빈 리스트 경우
    if lst.head is None:    # head가 None이면 시작을 할수없어
        print("none 이다")
        lst.head = new      # new는 100임 # 그렇기 떄문에 미리 만들어둔 new를 첫번째로 하여 시작
        # 첫 시작점을 잡아주는거
    else:                   # 리스트에 자료가 있을때
        # lst.head = 100을 cur에 할당
        cur = lst.head
        while cur.next is not None: # None을 찾을때까지 찾아야한다.
            cur = cur.next
            # print("++++++++++++")
        cur.next = new      # newsms 200
    print(new)
    lst.size+=1

#리스트 마지막에 추가하기2 tail 사용
def insertLast2(lst,new):
    # print를 돌려보면 tail은 계속해서 바뀐다. why? 실시간으로 맨뒤롤 바꿔주기 때문에!!
    print(lst.head,lst.tail,new)

    if lst.head is None:
        lst.head = lst.tail = new       # 맨처음엔 lst.head와 lst.tail이 none이기 때문에 lst.head(맨앞), lst.tail(맨뒤) 를 new(새로운 주소: 100)로 정의한다.
                                        # /None/None/ -> /100/100/ 보유값 : 0
    else:
        lst.tail.next = new             # 새로 만들어진 가상의 붕어빵틀인 lst.tailnext를 새로운 주소인 new로 할당
        lst.tail = new                  #  찐 tail을 항상 new(새로운 주소)로 할당하는것
    '''
    /100/200/ -> /200/200/  보유값 : 0, 1      여기서 lst.tail.next = new 역할이 첫번째 붕어빵틀에서 next의 값을 100 -> 200이고  lst.tail = new 역할은  200/200을 만들어냄
        0           1
    /100/200/ -> /200/300/ -> /300/300/  보유값 : 0, 1, 2
        0           1               2
    /100/200/ -> /200/300/ -> /300/400/ -> /400/400/  보유값 : 0, 1, 2, 3
        0           1               2           3
    /100/200/ -> /200/300/ -> /300/400/ -> /400/500/-> /500/500/  보유값 : 0, 1, 2, 3, 4
        0           1               2           3           4
    '''
    lst.size +=1

# n5 = Node(5)    # d=5라는 의미(d=5인 class Node를 n5에 담음)
# n4 = Node(4, n5)
# n3 = Node(3, n4)
# n2 = Node(2, n3)
# n1 = Node(1, n2)
# mylist.head = n1  # 기존 head = None에서 n1으로 변함 -> 맨처음을 n1으로 시작하겠다는 의미
# mylist.size = 5
#
# printList(mylist)

for i in range(5):
    insertLast2(mylist, Node(i))
    printList(mylist)