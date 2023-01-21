def hanoi(n, src, dist, via): # n: 남은장수, src: 현재위치, dist: 이동위치, via: 경유 장소
    if n > 1:
        hanoi(n-1, src, via, dist) # n-1장을 현재 위치에서 경유 장소로 옮김
        print(src + ' -> ' + dist)
        hanoi(n-1, via, dist, src) # n-1장을 경유 장소에서 이동 위치로 옮김
    else:
        print(src + ' -> ' + dist)

n = int(input())
hanoi(n, 'a', 'b', 'c')