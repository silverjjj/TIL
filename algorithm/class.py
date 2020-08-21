# 트라이 구조에 필요한 노드
class Node(object):
    def __init__(self,char, data=None):
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
        cur_node = self.head         # add를 통해 만든 trie 구조를 담은 dict

        for ch in word:
            # 노드를 타고 내려감
            if ch in cur_node.children:
                # 노드를 내려가다가 존재하면 해당 노드로 이동
                cur_node = cur_node.children[ch]
            else:
                return False

        if cur_node.data != None:
            return True

    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

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
            if curr.data != None:
                result.append(curr.data)

            queue += list(curr.children.values())

        return result
t = Trie()
def BOJ14425():
    N, M = map(int,input().split())
    for _ in range(N):
        word = input().rstrip()
        t.add(word)
    res = 0
    for _ in range(M):
        word2 = input().rstrip()
        if t.search(word2):
            res += 1
    print(res)
BOJ14425()