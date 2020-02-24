N = input().split()
print(N)
s = []
num = ['0','1','2','3','4','5','6','7','8','9','10']
sum = 0
a = ['+','-','*','/']
for i in range(len(N)-1):
    if N[i] in num:
        s.append(N[i])
    elif N[i] in a:
        print(s)
        a = int(s.pop())
        b = int(s.pop())
        if N[i] =='+':
            s.append(b+a)
        elif N[i] =='-':
            s.append(b-a)
        elif N[i] == '*':
            s.append(b*a)
        elif N[i] == '/':
            s.append(b/a)
    else:
        result = 'error'
print(s)