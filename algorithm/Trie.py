# 트라이 구조에 필요한 노드
class Node(object):
    def __init__(self, char, data=None):
        self.char = char
        self.data = data  # data is set to None if node is not the final char of string
        self.children = {}

class Trie(object):
    # 노드가 필요할때마다 Node 클래스에서 새로운 Node를 생성
    def __init__(self):
        self.head = Node(None)

    # word의 모든 문자를 트리구조처럼 만드는 함수
    def add(self, word):
        cur_node = self.head
        for ch in word:                         # word는 내가 넣는 문자열
            if ch not in cur_node.children:          # cur에 문자가 존재x
                # 해당 노드에 다음 문자열이 없으면 등록한다.
                cur_node.children[ch] = Node(ch)
            # 다음 노드로 이동
            cur_node = cur_node.children[ch]

        # 단어의 마지막에 도달할때 data에 word를 할당
        cur_node.data = word

    # 만들어진 cur_node에서 단어를 찾기위한 함수
    def search(self, word):
        cur_node = self.head                        # add 를 통해 만든 trie 구조를 담은 cur_node
        for ch in word:                             # 단어 한개씩 노드를 타고 내려감
            if ch in cur_node.children:             # 노드를 내려가다가 존재하면 해당 노드로 이동
                cur_node = cur_node.children[ch]    # 자식노드로 이동
            else:                                   # 없으면 False
                return False
        if (cur_node.data != None):                 # 맨 아래까지 도착하고, cur_node.data가 None이 아니라면
            return True                             # return True
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None
        print(curr_node,prefix)
        # Locate the prefix in the trie,
        # and make subtrie point to prefix's last character Node
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # Using BFS, traverse through the prefix subtrie,
        # and look for nodes with non-null data fields.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            # print(curr)
            if curr.data != None:
                result.append(curr.data)
            queue += list(curr.children.values())

        return result

t = Trie()      # Trie 클래스를 t객체로 사용, t는 Trie의 인스턴스
words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
for word in words:
    t.add(word)
# print(t.search("ulu"))
# print(t.search("ruler"))
# print(t.search("rulere"))
print(t.starts_with("ro"))