# Trie를 활용한 문자열 찾는 문제

# 트라이 구조에 필요한 노드
class Node(object):
    def __init__(self, char, data=None):
        self.char = char
        self.data = data  # data is set to None if node is not the final char of string
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def add(self, word):
        cur_node = self.head
        for ch in word:                         # word는 내가 넣는 문자열
            if ch not in cur_node.children:          # cur에 문자가 존재x
                # 해당 노드에 다음 문자열이 없으면 등록한다.
                cur_node.children[ch] = Node(ch)
            # 다음 노드로 이동
            cur_node = cur_node.children[ch]

        # 단어의 마지막에 도달할때
        cur_node.data = word

    def search(self, word):
        cur_node = self.head         # add 를 통해 만든 trie 구조를 담은 cur_node
        for ch in word:                             # 단어 한개씩 노드를 타고 내려감
            # print("다음 노드의 문자열 :", ch)
            if ch in cur_node.children:             # 노드를 내려가다가 존재하면 해당 노드로 이동
                cur_node = cur_node.children[ch]    # 자식노드로 이동
                # print("존재할경우 다음노드는? ",type(cur_node))
            else:                                   # 없으면 False
                return False
        if (cur_node.data != None):                 # 맨 아래까지 도착하고, cur_node.data가 None이라면
            return True


n,m = map(int,input().split())
t = Trie()
for _ in range(n):
    t.add(input())
char_list = []
for _ in range(m):
    char_list.append(input())
res = 0
for char in char_list:
    if t.search(char):
        res += 1
print(res)