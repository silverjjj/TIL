# 리스트 내포 가능을 이용해 피보나치 수열
# 10번째까지 출력하는 프로그램을 작성하십시오.

result = []

def fib(n):
    if n ==1 or n ==2:
        return 1
    return fib(n-1)+fib(n-2)

# for i in range(1,11):
#     fib(i)
#     result.append(fib(i))

result = [fib(i) for i in range (1,11)]
print(result)

