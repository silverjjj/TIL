T = int(input())

for test_case in range(1, T+1):
    month_s, day_s, month_f, day_f = map(int, input().split())
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result=0
    if month_s == month_f:
        result = day_f - day_s +1
    else:
        for i in range(month_s, month_f):
            result += month[i]

        result = result + day_f - day_s +1

    print(f"#{test_case} {result}")