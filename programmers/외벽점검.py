'''
둘레 n미터
취약한 지점들을 확인
점검시간을 1시간으로 제한
최소한의 친구들을 투입하여 취약지점 점검
'''
# def comb(dist,m,r,tr,comb_list):
#     if r == 0:
#         comb_list.append(tr[:])
#     elif r > m:
#         return
#     else:
#         tr[r-1] = dist[m-1]
#         comb(dist, m-1, r-1, tr,comb_list)
#         comb(dist, m-1, r, tr,comb_list)
#     return comb_list
# def find(weak,comb_list):
#     cnt = len(weak)
#     print(comb_list)
#     # while cnt:
#     #     cnt -= 1
#     #     inter_distance = []
#     #
#     # for row in comb_list:
#     #     print(r)


def find(weak,dist,m):
    print("=============================")
    print(weak,dist)
    L = len(weak)
    k = 0
    visitied = [0]*L
    for i in range(m):
        cur = dist[i]
        print("k ==>", k)
        for j in range(k,L-1):
            print(cur, weak[j + 1] - weak[j])
            if visitied[k]:
                k += 1
            if cur >= weak[j+1] - weak[j]:
                cur -= (weak[j+1] - weak[j])
                visitied[j] = visitied[j+1] = 1
                k = j+1
                print("cur ==>" , cur)
            else:
                break

            print(visitied)
def solution(n, weak, dist):
    answer = 0
    m = len(dist)
    dist = dist[::-1]
    for i in range(m):
        find(weak,dist,m)
        num = weak.pop(0)
        weak.append(n+num)
    return answer


n = 12
weak =[1, 5, 6, 10]
dist = [1, 2, 3, 4]
solution(n, weak, dist)