a = [[3, 3, 5, 2, 9],
     [3, 3, 8, 3, 1],
     [4, 4, 0, 1, 4],
     [3, 3, 1, 2, 7],
     [1, 3, 8, 3, 3]]
zero = [[0]*5 for i in range(5)]

xy = []
for row in a:
    zero[row[0]][row[1]] += 1
    if zero[row[0]][row[1]] >= 2:
        if [row[0],row[1]] not in xy:
            xy.append([row[0],row[1]])

print(xy)

xa = 3
ya = 3
lst = []
for x,y,s,d,z in a:
    if xa == x and y == ya:
        lst.append(z)

print(lst)
ma = max(lst)
if ma in lst:
    lst.remove(ma)
print(lst)
for row in a:
    for l in lst:
        if l == row[-1]:
            a.remove(row)
print(a)