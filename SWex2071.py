list_n = []
a = int(input())
for i in range(a):
    k = input().split()
    list_n.append(k)

for j in range(a):
    if len(list_n[j]) == 10:
        print(f"#{j+1}",end = " ")
        list_n[j] = list(map(int, list_n[j]))
        sum = 0
        for num in list_n[j]:
            sum += num
            avg = sum/len(list_n[j])
        print(round(avg))
    else:
        0
