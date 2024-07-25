import sys

input = sys.stdin.readline

N, K = map(int, input().split())
words = [set(input().rstrip()) for _ in range(N)]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # idx [0]: a / [25]: z
answer = 0

if K < 5:
    print(0)
    exit()
elif K == 26:  # 모든 알파벳을 다 가르칠 수 있으므로 모든 단어를 가르침
    print(N)
    exit()

learned = [0] * 26
for i in ('a', 'n', 't', 'i', 'c'):
    learned[alphabet.index(i)] = 1


def dfs(idx, cnt):
    global answer
    if cnt == K - 5:
        readcnt = 0

        for word in words:  # 제일 처음에 idx가 b 기준으로 단어 탐색
            flag = True
            for w in word:
                if not learned[alphabet.index(w)]:
                    flag = False
                    break
            if flag:  # 단어를 읽을 수 있다면 (다 배운 알파벳으로만 있다면)
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not learned[i]:  # 알파벳 a 부터 배우지 않았다면 몇개의 단어를 배울 수 있는지 탐색
            learned[i] = 1
            dfs(i, cnt + 1)
            learned[i] = 0


dfs(0, 0)
print(answer)