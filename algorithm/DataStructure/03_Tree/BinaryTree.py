class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None    # Tree 클래스에 처음 들어올때 root값을 None으로 정의

    def preorderTraversal(self, node):
        print(node, end='')
        # print(type(node), type(node.left), type(node.right))
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left  == None : self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        print(node)
        node.left = left_node
        node.right = right_node

if __name__ == "__main__":
    # Node 클래스에서 1~7까지의 각각의 노드값을 만든다.
    node = []
    node.append(Node('1'))
    node.append(Node('2'))
    node.append(Node('3'))
    node.append(Node('4'))
    node.append(Node('5'))
    node.append(Node('6'))
    node.append(Node('7'))
    print(node)
    t = Tree()
    for i in range(int(len(node)/2)):
        print(node[i],node[i*2+1],node[i*2+2])
        t.makeRoot(node[i],node[i*2+1],node[i*2+2])
    print('전위 순회 : ', end='') ; t.preorderTraversal(t.root)
    print('\n' + '중위 순회 : ', end='') ; t.inorderTraversal(t.root)
    print('\n' + '후위 순회 : ', end='') ; t.postorderTraversal(t.root)