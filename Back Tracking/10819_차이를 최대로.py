import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
answer2 = 0
visited = [0] * N


def solution1():
    answer = 0
    results = permutations(nums, N)

    for i in results:
        total = 0
        for num in range(N - 1):
            total += abs(i[num] - i[num + 1])

        if total > answer:
            answer = total
        else:
            continue
    return answer


def dfs(arr):
    global answer2

    if len(arr) == N:
        total = 0
        for i in range(N - 1):
            total += abs(arr[i] - arr[i + 1])
        answer2 = max(answer2, total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            arr.append(nums[i])
            dfs(arr)
            visited[i] = 0
            arr.pop()


dfs([])
print(answer2)
