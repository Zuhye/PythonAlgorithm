import sys

input = sys.stdin.readline

N = int(input())
energy = list(map(int, input().split()))
answer = 0


def dfs(x):
    global answer

    if len(energy) == 2:
        answer = max(answer, x)
        return

    for i in range(1, len(energy) - 1):
        value = energy[i - 1] * energy[i + 1]

        # 백트래킹
        v = energy.pop(i)
        dfs(x + value)
        energy.insert(i, v)


dfs(0)
print(answer)