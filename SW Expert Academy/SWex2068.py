T = int(input())

for i in range(0,T):
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = map(int, input().split())
    print(f"#{i+1}",max(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))
