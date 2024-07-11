import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    words = [list(input().rstrip()) for _ in range(N)]
    alphabet = ['a', 'c', 'i', 'n', 't']
    answer = 0

    if K < 5:
        print(0)
        exit(0)
    else:
        K -= 5

    results = []
    for i in words:
        temp = i[4:-4]

        filter_temp = []
        for ch in temp:
            if ch not in alphabet:
                filter_temp.append(ch)
        if not filter_temp:
            answer += 1
        else:
            results.append(filter_temp)

    results.sort(key=lambda x: (len(x), x))

    while K > 0:
        for i in results:
            for j in i:
                if j not in alphabet:
                    if len(i) <= K:
                        alphabet.append(j)
                        K -= 1
                        i.pop(0)
                else:
                    i.pop(0)

            if len(i) == 0:
                answer += 1

    print(answer)


# -------------------------- 답지 참조 -------------------

def solution2():
    n, k = map(int, input().split())
    words = [set(input().rstrip()) for _ in range(n)]

    if k < 5:
        print(0)
        exit()
    elif k == 26:
        print(n)
        exit()
    global answer
    answer = 0
    learned = [0] * 26

    for i in ('a', 'c', 't', 'i', 'n'):
        learned[ord(i) - ord('a')] = 1  # [0] 자리부터 a로 두기 위해

    def dfs(idx, cnt):
        global answer

        if cnt == k - 5:
            readcnt = 0

            for word in words:
                flag = True
                for w in word:
                    if not learned[ord(w) - ord('a')]:
                        flag = False
                        break
                if flag:
                    readcnt += 1

            answer = max(answer, readcnt)
            return

        for i in range(idx, 26):
            if not learned[i]:
                learned[i] = True
                dfs(i, cnt + 1)
                learned[i] = False

    dfs(0, 0)
    print(answer)


solution2()
