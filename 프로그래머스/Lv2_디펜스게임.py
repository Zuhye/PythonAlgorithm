import heapq


def solution(n, k, enemy):
    heap = []

    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(heap, -enemy[i])  # 최대힙

        if n < 0:
            if k > 0:
                n += -heapq.heappop(heap)
                k -= 1
            else:
                return i
    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# 5 출력
print(solution(2, 4, [3, 3, 3, 3]))
# 4출력
