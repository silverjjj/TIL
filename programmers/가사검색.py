from collections import defaultdict
class Node(object):
    def __init__(self, char, data=None):
        self.char = char
        self.data = data
        self.children = {}
        self.length = defaultdict(int)  # defaultdict: 인지값이 없으면 0으로 리턴

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        curr_node = self.head
        curr_node.length[len(word)] += 1            # 맨위 노드에 문자열의 길이의 개수를 다 저장해놓음
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = Node(ch)   # 다음 노드에 등록
            curr_node.children[ch].length[len(word)] += 1   # 해당 노드를 거쳐가는 문자열 중 길이가 len(word) 인것의 개수를 += 1해줌
            curr_node = curr_node.children[ch]      # 다음 노드로 이동

        curr_node.data = word  #문자를 가장 아래 노드에 data변수로 넣는다

    def search(self, prefix, length):
        curr_node = self.head
        for ch in prefix:
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            else:
                return 0
        # prefix의 마지막 노드에서 length 변수를 확인하여 길이가 length인것의 개수를 반환
        c = curr_node.children
        return curr_node.length[length]

def solution(words, queries):
    answer = []
    # Trie를 2가지 만들어, 비교할 문자의 ? 위치에 따라 확인해준다.
    front = Trie()
    back = Trie()
    for word in words:
        front.insert(word)
        back.insert(word[::-1])

    for querie in queries:
        if querie == "?"*len(querie):
            answer.append(front.head.length[len(querie)])
        elif querie[0] == "?":
            word = querie[::-1]
            word = word[:word.find("?")]
            answer.append(back.search(word,len(querie)))
        else:
            word = querie[:querie.find("?")]
            answer.append(front.search(word, len(querie)))
    return answer