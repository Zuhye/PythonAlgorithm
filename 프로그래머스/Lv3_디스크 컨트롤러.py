import heapq


def solution(jobs):
    answer = 0
    now = 0  # 현재 시간
    cnt = 0  # 처리해야 할 작업 수
    start = -1  # 이전 작업의 시작시간
    heap = []

    while cnt != len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heapq.heappush(heap, (i[1], i[0]))
        if heap:
            tmp = heapq.heappop(heap)
            start = now
            now += tmp[0]
            cnt += 1  # 작업 하나 처리
            answer += now - tmp[1]  # 소요시간
        else:
            now += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))