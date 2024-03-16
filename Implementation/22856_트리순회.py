import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 파이썬의 재귀 최대 깊이 설정

N = int(input())
tree = {}
visited = [False] * (N + 1)
visited2 = [False] * (N + 1)
cnt = [0, 0]

for i in range(N):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]


def inorder1(node):
    global cnt
    visited[node] = True

    if not visited[tree[node][0]] and tree[node][0] != -1:  # 왼쪽 자식 방문
        inorder1(tree[node][0])
        cnt[0] += 1
    if not visited[tree[node][1]] and tree[node][1] != -1:  # 오른쪽 자식 방문
        inorder1(tree[node][1])
        cnt[0] += 1


def inorder2(node):
    global cnt
    visited2[node] = True

    if not visited2[tree[node][1]] and tree[node][1] != -1:
        inorder2(tree[node][1])
        cnt[1] += 1


inorder1(1)
inorder2(1)
print(2*cnt[0] - cnt[1])
