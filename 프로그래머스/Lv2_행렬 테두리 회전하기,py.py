def solution(rows, columns, queries):
    answer = []
    board = [[0] * columns for _ in range(rows)]
    value = 1  # 첫 번째 칸에 채울 값
    for i in range(rows):
        for j in range(columns):
            board[i][j] = value
            value += 1

    for queries in queries:
        x1, y1, x2, y2 = queries
        start_point = board[x1 - 1][y1 - 1]
        min_value = start_point

        for k in range(x1 - 1, x2 - 1):  # 가장 왼쪽 세로 한칸 씩 이동
            tmp = board[k + 1][y1 - 1]
            board[k][y1 - 1] = tmp
            min_value = min(min_value, tmp)

        for k in range(y1 - 1, y2 - 1):  # 가장 아래 가로 한칸 씩 이동
            tmp = board[x2 - 1][k + 1]
            board[x2 - 1][k] = tmp
            min_value = min(min_value, tmp)

        for k in range(x2 - 1, x1 - 1, -1):  # 가장 오른쪽 세로 한칸 씩 이동
            tmp = board[k - 1][y2 - 1]
            board[k][y2 - 1] = tmp
            min_value = min(min_value, tmp)

        for k in range(y2 - 1, y1 - 1, -1):
            tmp = board[x1 - 1][k - 1]
            board[x1 - 1][k] = tmp
            min_value = min(min_value, tmp)

        board[x1 - 1][y1] = start_point
        answer.append(min_value)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# [8, 10, 25] 출력
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# [1, 1, 5, 3] 출력
print(solution(100, 97, [[1, 1, 100, 97]]))
# [1] 출력
