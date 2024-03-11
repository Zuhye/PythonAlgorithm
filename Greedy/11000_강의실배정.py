import sys
import heapq

input = sys.stdin.readline

N = int(input())
time = []
heap = []

for _ in range(N):
    s, t = map(int, input().split())
    time.append((s, t))

time.sort(key=lambda x: x[0])
heapq.heappush(heap, time[0][1])

for i in range(1, N):
    if heap[0] > time[i][0]:
        heapq.heappush(heap, time[i][1]) # 새 강의실을 사용해야 하는 경우
    else:
        heapq.heappop(heap) # 제일 첫 강의실 사용
        heapq.heappush(heap, time[i][1])

print(len(heap))