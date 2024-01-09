# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

N = int(input())
visited = [False] * N
result = []


def check(x, col):
    for i, row in enumerate(reversed(col)):
        if (x - i - 1 == row) or (x + i + 1 == row):
            return False

    return True


def search(col):
    if len(col) == N:  # 전부 배치되면 출력
        result.append(col)
        return

    for i in range(N):
        if visited[i]:
            continue

        if i not in col:  # 동일한 행은 사용하지 않음
            if check(i, col):
                col.append(i)
                visited[i] = True
                search(col)
                visited[i] = False
                col.pop()  # N 바퀴 돈 후 더이상 자리 없으면 뺀다


search([])
print(len(result))