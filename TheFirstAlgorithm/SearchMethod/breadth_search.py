tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

data = [0]
data2 = [0]

while len(data) > 0:
    pos = data.pop(0)
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)
print("\n")


# 전위 순회
def search(pos):
    print(pos, end=' ')
    for i in tree[pos]:
        search(i)
search(0)
print("\n")

# 후위 순회
def search2(pos):
    for i in tree[pos]:
        search(i)
    print(pos, end=' ')
search2(0)
print("\n")

# 중위 순회
def search3(pos):
    if len(tree[pos])==2:
        search3(tree[pos][0])
        print(pos, end=' ') # 왼쪽 노드와 오른쪽 노드 사이에 출력
        search3(tree[pos][1])
    elif len(tree[pos]) == 1:
        search3(tree[pos][0])
        print(pos, end=' ')
    else:
        print(pos, end=' ')
search3(0)
print("\n")

#후위 순위 반대(재귀 X)
while len(data2) > 0:
    pos = data2.pop()
    print(pos, end=' ')
    for i in tree[pos]:
        data2.append(i)
print("\n")