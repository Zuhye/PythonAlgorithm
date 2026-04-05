def solution(n, t, m, timetable):
    answer = ''
    bus = ["09:00"]
    timetable.sort()

    if n > 1:
        for i in range(1, n):
            hour, minute = map(int, bus[i - 1].split(":"))
            total = hour * 60 + minute + t
            new_hour = total // 60
            new_minute = total % 60

            if new_minute < 10:
                new_minute = "0" + str(new_minute)
            else:
                new_minute = str(new_minute)

            if new_hour < 10:
                new_hour = "0" + str(new_hour)
            else:
                new_hour = str(new_hour)

            new_time = str(new_hour) + ":" + str(new_minute)

            bus.append(new_time)

    for i in range(n):
        b = bus[i]
        tmp = []
        while timetable:
            if len(tmp) == m:
                break

            if timetable[0] <= b:
                tmp.append(timetable.pop(0))
            else:
                break

        if i == n - 1:  # 마지막 버스
            if len(tmp) < m:
                return b
            else:
                hour, minute = map(int, tmp[-1].split(":"))
                total = hour * 60 + minute - 1

                new_hour = total // 60
                new_minute = total % 60

                if new_hour < 10:
                    new_hour = "0" + str(new_hour)
                else:
                    new_hour = str(new_hour)

                if new_minute < 10:
                    new_minute = "0" + str(new_minute)
                else:
                    new_minute = str(new_minute)

                return new_hour + ":" + new_minute


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))  # 답: "09:00"
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))  # 답: "09:09"
