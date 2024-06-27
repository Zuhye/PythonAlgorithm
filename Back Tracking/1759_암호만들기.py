import sys

input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = input().split()
alphabet.sort()
#  Lookup table 모음 저장
tbl = [0] * 128
for ch in "aeiou":
    tbl[ord(ch)] = 1


def dfs(n, cnt, tst):
    if n == C:  # 모든 알파벳의 사용 여부를 선택한 경우
        if len(tst) == L and cnt >= 1 and L - cnt >= 2:  # 모든 조건 만족
            ans.append(tst)
        return

    # 포함하는 경우
    dfs(n + 1, cnt + tbl[ord(alphabet[n])], tst + alphabet[n])
    # 포함하지 않는 경우
    dfs(n + 1, cnt, tst)


# n(index), cnt(모음의 개수), tst(완성되는 문자열)
ans = []
dfs(0, 0, "")
for i in ans:
    print(i)
