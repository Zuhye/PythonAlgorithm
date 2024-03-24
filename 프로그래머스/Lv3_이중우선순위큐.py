import heapq


def solution(operations):
    answer = [0, 0]
    heap = []
    for i in operations:
        operation = i.split(" ")
        if operation[0] == "I":  # 숫자 삽입
            heapq.heappush(heap, int(operation[1]))
        else:
            if len(heap) == 0:
                pass
            elif operation[0] == "D" and operation[1] == "-1":  # 최솟값 삭제
                heapq.heappop(heap)
            elif operation[0] == "D" and operation[1] == "1":  # 최대값 삭제
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)  # 다시 힙 형태로 변경

    if len(heap) != 0:
        answer[0] = max(heap)
        answer[1] = min(heap)

    return answer


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
