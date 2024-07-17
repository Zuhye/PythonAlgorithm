import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())  # N: 보석 개수 / K: 가방 개수
jewerly = []

for _ in range(N):
    m, v = map(int, input().split())
    jewerly.append([m, v])
bags = list(int(input()) for _ in range(K))

jewerly.sort() # 보석 무게를 기준으로 정렬
bags.sort()

answer = []
value = 0
j = 0  # 보석 탐색하는 idx

for i in bags:
    while j < N and jewerly[j][0] <= i:
        heapq.heappush(answer, -jewerly[j][1])
        j += 1

    if answer:
        value += -heapq.heappop(answer)

print(value)