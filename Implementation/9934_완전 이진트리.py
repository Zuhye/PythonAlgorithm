import sys

input = sys.stdin.readline

K = int(input())
arr = list(map(int, input().split()))
length = len(arr)

tree = [[] for _ in range(K)]


def dfs(first, last, K):
    if first == last:
        tree[K].append(arr[first])
        return
    mid = (first + last) // 2  # 배열의 중앙 값이 루트 노드
    tree[K].append(arr[mid])

    dfs(first, mid - 1, K + 1)
    dfs(mid + 1, last, K + 1)


dfs(0, length - 1, 0)

for i in tree:
    print(*i)
