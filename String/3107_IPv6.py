import sys

input = sys.stdin.readline
result = ''
N = str(input().rstrip("\n"))
words = N.split(":")

if '' in words:

    if N.startswith("::"):
        rest = len(words[2:])
        words = ['0000'] * (8-rest) + words[2:]

    elif N.endswith("::"):
        rest = len(words[:-2])
        words = words[:-2] + ['0000'] * (8 - rest)

    else:
        idx = words.index('')
        while '' in words:
            words.remove('')
        rest = len(words)
        words = words[:idx] + ['0000'] * (8 - rest) + words[idx:]

for i in range(len(words)):
    words[i] = words[i].zfill(4)

print(":".join(words))