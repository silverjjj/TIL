import random, datetime, threading, time


def calc():
    max([random.random() for i in range(5000000)])
    max([random.random() for i in range(5000000)])
    max([random.random() for i in range(5000000)])


# 1 Thread : 두개의 함수를 하나의 쓰레드에서 연속적으로 실행
start_time = datetime.datetime.now()
calc()
calc()
end_time = datetime.datetime.now()
print(end_time - start_time)

# 2 Threads : 쓰레드를 2개 생성해서 쓰레드에서 하나씩 실행
start_time = datetime.datetime.now()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=calc))
    threads[-1].start()

for t in threads:
    t.join()

end_time = datetime.datetime.now()
print(end_time - start_time)

'''
각각 6초, 7초걸림
멀티 쓰레딩이 시간이 더걸림
이런 결과가 나온 이유는 파이썬에서 Global Interpreter Lock이라고 부르는 동기화 방식 때문

'''