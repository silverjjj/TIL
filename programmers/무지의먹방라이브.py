import heapq
def solution(food_times, k):
    # 힙을 활용
    hq = []
    # food_times의 음식 크기와 idx를 함께 hq에 넣어준다
    for idx, num in enumerate(food_times):
        heapq.heappush(hq,[num, idx+1])
    prev_num = 0
    # 가장 음식크기가 작은값을 small_num에 할당
    small_num = hq[0][0]
    while k - ((small_num - prev_num) * len(hq)) >= 0:
        # small_num - prev_num을 해주는 이유는 현재 음식의 크기에서 이전의 음식크기의 차이만 k를 빼주기 위해
        k -= (small_num - prev_num) * len(hq)
        # hq내에서 num의 값이 가장 작은것(음식의 크기가 가장 작은것)을 pop해서 prev_num에 할당
        prev_num, idx = heapq.heappop(hq)
        if not hq:
            return -1
        # 현재 hq내에서 가장 작은 음식을 small_num 에 할당
        small_num = hq[0][0]
    # idx를 기준으로 정렬
    hq.sort(key = lambda x : x[1])
    return hq[k % len(hq)][1]

food_times = [3,1,2]
k = 5
print(solution(food_times, k))