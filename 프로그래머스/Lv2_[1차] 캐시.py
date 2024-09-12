def solution(cacheSize, cities):
    answer = 0
    stack = []

    if cacheSize == 0:
        answer = len(cities) * 5
        return answer

    for i in range(len(cities)):
        if cities[i].lower() not in stack and len(stack) < cacheSize:
            stack.append(cities[i].lower())
            answer += 5
        elif cities[i].lower() in stack:
            answer += 1
            stack.remove(cities[i].lower())
            stack.append(cities[i].lower())
        elif cities[i].lower() not in stack and len(stack) == cacheSize:
            answer += 5
            stack.pop(0)
            stack.append(cities[i].lower())

    return answer


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16출력
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50 출력
