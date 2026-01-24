import sys

num = int(input())
tree = {}

for _ in range(num) :
    root, left, right = input().split()
    tree[root] = [left, right]

def pre(node) : # V -> L -> R
    if node == '.' :
        return
    print(node, end='') # 먼저 자기 자신 먼저 출력함
    pre(tree[node][0]) # 좌측 탐색
    pre(tree[node][1]) # 마지막 순서로 우측 탐색
     
def ino(node) : # L -> V -> R
    if node == '.' :
        return
    ino(tree[node][0]) # 좌측 먼저 탐색
    print(node, end='') # 자기 자신 출력
    ino(tree[node][1]) # 마지막 우측 탐색

def post(node) : # L -> R -> V
    if node == '.' :
        return
    post(tree[node][0]) # 좌측 먼저 탐색
    post(tree[node][1]) # 우측 탐색
    print(node, end='') # 마지막으로 자신 출력

# 항상 루트노드는 'A'로 시작
pre('A')
print()

ino('A')
print()

post('A')