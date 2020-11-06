# def is_prime_not_bad(n:int):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     l = round(n**0.5) + 1
#     print(l)
#     for i in range(3,l,2):
#         if n % i == 0:
#             return False
#     return True
# time = len([x for x in range(1, 100000) if is_prime_not_bad(x)])
# print(time)
m = 17
l= round(m**0.5)+1
print(l)