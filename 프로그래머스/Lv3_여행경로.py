from collections import deque


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))

    # 현재 경로와 남은 티켓을 큐에 저장
    q = deque([(["ICN"], tickets)])

    while q:
        path, ticket = q.popleft()

        if len(ticket) == 0:
            answer = path
            break

        # 출발지가 현재 위치한 공항과 같은 티켓 중 가장 왼쪽 거
        idx = -1
        for i in range(len(ticket)):
            if ticket[i][0] == path[-1]:
                idx = i
                break

        if idx == -1:
            continue

        while idx < len(ticket) and ticket[idx][0] == path[-1]:
            q.append((path + [ticket[idx][1]], ticket[:idx] + ticket[idx + 1:]))
            idx += 1

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "JFK", "HND", "IAD"]
