import copy
def empty_lock(lock,n,m):
    empty = []  # 자물쇠가 빈부분
    filled = [] # 자물쇠가 있는부분
    for i in range(n):
        for j in range(n):
            if not lock[i][j]:
                empty.append([i+m-1,j+m-1])
            else:
                filled.append([i+m-1,j+m-1])
    return tuple(empty), tuple(filled)

def find(one_list,e,empty,filled):
    for i in range(e):
        for j in range(e):
            key_move = []  # 열쇠의 위치를 이동
            for x,y in one_list:
                if 0<=x+i<e and 0<= y+j<e:
                    key_move.append([x+i,y+j])
                else:
                    break
            if len(key_move) == len(one_list):
                key_move = tuple(key_move)
                flag = True

                for zero in empty:
                    if zero in key_move:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    for one in filled:
                        if one in key_move:
                            flag = False
                            break
                    if flag:
                        return True
    return False

def rotate_90(key,empty,m,e,filled):
    ret = copy.deepcopy(key)
    for _ in range(4):
        one_list = []
        # 한바퀴 씩 돌리면서 확인해봄
        tmp = [[0] * m for _ in range(m)]
        for x in range(m):
            for y in range(m):
                tmp[y][m - 1 - x] = ret[x][y]
                if tmp[y][m - 1 - x] == 1:
                    one_list.append([y,m - 1 - x])
        ret = tmp.copy()
        if find(one_list,e,empty,filled):
            return True
    return False

def solution(key, lock):
    n = len(lock)
    m = len(key)
    empty,filled = empty_lock(lock,n,m)
    e = (m - 1) * 2 + n
    answer = rotate_90(key,empty,m,e,filled)
    return answer