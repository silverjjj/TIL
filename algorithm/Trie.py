# 1. Node 구현
class Node(object):
    def __init__(self, key, data=None):
        # print('4444')
        self.key = key  # key는 단어의 글자 한개 담는데 사용됨
        self.data = data
        self.children = {}
        print(self.key, self.data, self.children)

# 2. Trie 구현
class Trie(object):
    def __init__(self):
        self.head = Node(None)
    '''
    트라이에 문자열 삽입
    '''
    def insert(self, string):
        curr_node = self.head
        # print(curr_node,'의', curr_node.children)
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
                # print("===========")
                # print(curr_node.children[char],Node(char))
            curr_node = curr_node.children[char]

            # string 의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string
        # print('string ==>',string)
    """
    Returns if string exists in the trie
    """
    def search(self, string):
        print('3333')
        curr_node = self.head
        print(self.head)
        print(curr_node)
        print(curr_node.children)
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # Reached the end of string,
        # If curr_node has data (i.e. curr_node is not None), string exists in the trie
        if (curr_node.data != None):
            return True


# Test
t = Trie()
words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
for word in words:
    t.insert(word)

print(t.search("romulus"))
# print(t.search("ruler"))
# print(t.search("rulere"))
# print(t.search("romunus"))
# print(t.starts_with("ro"))
# print(t.starts_with("rube"))