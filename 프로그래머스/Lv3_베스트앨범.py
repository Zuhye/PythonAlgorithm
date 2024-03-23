def solution(genres, plays):
    answer = []
    dic = {}
    for i, genre_play in enumerate(zip(genres, plays)):
        genre, play = genre_play
        if genre not in dic:
            dic[genre] = {'total': 0, 'song': []}
        dic[genre]['total'] += play
        dic[genre]['song'].append((i, play))
    for i in dic:
        dic[i]['song'].sort(key=lambda x: (-x[1], x[0]))  # 횟수 내림차순, idx 오름차순

    result = sorted(dic.items(), key=lambda x: x[1]['total'], reverse=True)

    for genre, value in result:
        for i in value['song'][:2]:  # 최대 2곡 까지
            answer.append(i[0])  # index 삽입

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
