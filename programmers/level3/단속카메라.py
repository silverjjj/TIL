'''
모든 차량이 한번은 카메라를 만나야함 ,, 최소 몇대 카메라를 설치해야하냐 ?

'''
def solution(routes):
    answer = 1
    routes.sort()
    standard = 30000
    for route in routes:
        if route[0] <= standard:
            standard = min(route[1], standard)
        else:
            standard = route[1]
            answer += 1
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)