bases = str(input())
case = []
for i in bases:
    case.append(i)
print(case)
card = []
for i in range(0,len(bases),3):
    card.append(bases[i:i+3])
print(card)
a = list(set(card))
print(a)

if len(a) == len(card):
