'''
콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
'''
num = input()

num_list =list(map(int,num.split(',')))
print(num_list)

num_tuple =tuple(map(int,num.split(',')))
print(num_tuple)
