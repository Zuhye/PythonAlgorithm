from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while bridge:
        bridge.pop(0)
        answer += 1
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
