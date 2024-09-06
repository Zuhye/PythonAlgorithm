import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())
sets = [input().rstrip() for _ in range(N)]
search = [input().rstrip() for _ in range(M)]

sets.sort()

answer = 0

for s in search:
    # 이진 탐색으로 sets 리스트에서 s보다 같거나 큰 첫 번째 위치를 찾음
    pos = bisect_left(sets, s)

    # pos가 유효한 범위 안에 있고 해당 위치에서 접두사 검사
    if pos < N and sets[pos].startswith(s):
        answer += 1

print(answer)