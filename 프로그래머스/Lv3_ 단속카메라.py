def solution(routes):
    routes.sort(key=lambda x: x[0])

    value = routes[0][1]
    answer = 1

    for i in range(1, len(routes)):
        if routes[i][0] <= value:
            value = min(routes[i][1], value)
        else:
            value = routes[i][1]
            answer += 1

    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #  2 출력
