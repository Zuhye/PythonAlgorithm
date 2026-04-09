def solution(info, edges):
    answer = []
    visited = [False] * len(info)

    def dfs(sheep, wolves):
        if sheep > wolves:
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep + 1, wolves)
                else:
                    dfs(sheep, wolves + 1)
                visited[c] = False

    visited[0] = True
    dfs(1, 0)  # 제일 처음에 양 1 / 늑대 0 으로 시작

    return max(answer)


# 답: 5
print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))

# 답: 5
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))