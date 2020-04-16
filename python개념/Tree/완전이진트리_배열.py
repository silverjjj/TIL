'''
부모인덱스가 i일때
왼쪽자식 : 2*i
오른쪽 자식 2*i+1

현재노드의 부모 인덱스 : i//2
root는 1부터 시작함
'''

# 전위순회 : V(현재노드) -> L(왼쪽) -> R(오른) 순서대로 순회한다/
def preOrder(idx):  #맨처음 idx = 1 로시작 (tree[1] 을뽑아냄)
    if idx <= lastidx:
        print(tree[idx], end = " ")
        preOrder(2*idx)     #왼쪽자식으로 이동한뒤 현재위치를 왼쪽자식으로
        preOrder(2*idx+1)

def add(n):     #완전이진트리를 채움 -> 마지막노드에 채움
    global lastidx      #global은 전역변수에 정의되있는걸 사용하기위해
    lastidx += 1
    tree[lastidx] = n

size = 15
tree = [0]*(size+1)
lastidx = 0

for i in range(0,10):
    add(chr(i+65))      # 아스키코드를 이용
print(tree)
preOrder(1)