'''
1. 재생된 장르가 많은 순서
2. 재생된 노래
3. 재생횟수가 같다면 고유번호가 낮은 노래

장르별로 2개씩 노래를 추출
'''
def solution(genres, plays):
    answer = []
    albums = {}
    n = len(genres)
    for i in range(n):
        genre = genres[i]; play = plays[i]
        if genre not in tuple(albums.keys()):
            albums[genre] = [[i, play]]
        else:
            albums[genre].append([i, play])
    arr = []
    for key, value in albums.items():
        res = 0
        for v in value:
            res += v[1]
        arr.append([key, res])
    arr = sorted(arr, key=lambda x: -x[1])
    for genre, total_cnt in arr:
        song = sorted(albums[genre], key = lambda x: (-x[1], x[0]))
        song = song[:2]
        for num, cnt in song:
            answer.append(num)
    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [800, 600, 800, 900, 2500]
solution(genres, plays)