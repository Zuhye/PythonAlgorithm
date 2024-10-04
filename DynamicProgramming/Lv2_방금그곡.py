# 멜로디가 arr에 있는지 확인
def check(remember, arr):
    for i in range(len(arr) - len(remember) + 1):
        if arr[i:i + len(remember)] == remember:
            return True
    return False


def solution(m, musicinfos):
    answer = []
    result = ""
    songs = {}

    # 기억한 멜로디도 # 처리를 해줘야 합니다.
    temp_m = []
    for i in range(len(m)):
        if i < len(m) - 1 and m[i + 1] == "#":
            temp_m.append(m[i] + "#")
        elif m[i] != "#":
            temp_m.append(m[i])

    for idx, v in enumerate(musicinfos):
        start, end, title, melody = v.split(',')
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        time = (eh * 60 + em) - (sh * 60 + sm)
        temp = []
        for i, v in enumerate(melody):
            if v == "#":
                temp.pop()
                temp.append(melody[i - 1] + melody[i])
            else:
                temp.append(melody[i])

        if len(temp) > time:
            songs[title] = (temp[:time], time, idx)
        else:
            songs[title] = (temp * (time // len(temp)) + temp[:time % len(temp)], time, idx)

    for i, v in songs.items():
        if check(temp_m, v[0]):
            answer.append((i, v[1], v[2]))

    if len(answer) == 0:
        result = "(None)"
    else:
        answer.sort(key=lambda x: (-x[1], x[2]))
        result = answer[0][0]
    return result


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# HELLO 출력
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# FOO 출력
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# WORLD 출력
