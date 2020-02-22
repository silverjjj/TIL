A, B = map(int, input().split())
numbers = []
for i in range(A, B + 1):
    numbers.append(i)
def is_prime(A,B):
    result = []
    for i in numbers:
        if i % 2==0:
            if i == 2:
                result.append(i)
            else:
                numbers.remove(i)
        elif i %