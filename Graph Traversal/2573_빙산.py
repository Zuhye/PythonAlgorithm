from collections import deque

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# time = 0
#
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = 1
#
#     while q:
#         cx, cy = q.popleft()
#         for d in range(4):
#             nx = cx + dir[d][0]
#             ny = cy + dir[d][1]
#
#             if 0 <= nx < N and 0 <= ny < M:
#                 if board[nx][ny] != 0 and not visited[nx][ny]:  # 방문하지 않은 빙산이면
#                     q.append((nx, ny))
#                     visited[nx][ny] = 1
#                 elif board[nx][ny] == 0:  # 주변이 바다이면 개수 확인해야 함
#                     visited[cx][cy] += 1
#
#
# while True:
#     cnt = 0  # 녹인 빙산 개수
#     visited = [[0] * M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j] and board[i][j] != 0:
#                 bfs(i, j)
#                 cnt += 1
#
#     # 주면 바다 개수 만큼 녹이기
#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] != 0:
#                 board[i][j] -= (visited[i][j] - 1)
#                 if board[i][j] < 0:
#                     board[i][j] = 0
#     if cnt >= 2:
#         print(time)
#         break
#     if cnt == 0:
#         print(0)
#         break
#
#     time += 1


######  방법 2 ##########


def bfs2(si, sj, v):
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        #  네 방향, 범위내(X), 미방문,  > 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if v[ni][nj] == 0 and arr[ni][nj] > 0:
                q.append((ni, nj))
                v[ni][nj] = 1


def solve():  # 1년 부터 90000 년 전체 순회
    for year in range(1, 900000):
        # [1] 네방향 0의 개수 카운트
        a_sub = [[0] * M for _ in range(N)]
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j] == 0:
                    continue
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 0:
                        a_sub[i][j] += 1

        # [2] 높이 낮추기
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if a_sub[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - a_sub[i][j])

        # [3] 빙산의 덩어리 개수 카운트
        v = [[0] * M for _ in range(N)]
        count = 0
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if v[i][j] == 0 and arr[i][j] > 0:  # 빙산인데 방문한 적이 없다면
                    bfs2(i, j, v)
                    count += 1

                    if count > 1:  # 두 덩어리 이상..
                        return year
        if count == 0:
            return 0
    # 이 자리에 올 일은 없지만..
    return -1


arr = [list(map(int, input().split())) for _ in range(N)]
ans = solve()
print(ans)
