'''
암호는 서로 다른 L개의 알파벳 소문자
최소 1개의 모음 + 두개의 자음으로 구성
암호에서 알파벳 순서로 배열
C가지의 문자종류가 있는데
가능성 있는 암호를 모두 구하자
겹침 X
7퍼에서 틀림
'''
import sys
read = sys.stdin.readline
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
aeiou = set(['a','e','i','o','u'])

def combination(r,C):
    if r == 0:
        res.append(tr[:])
    elif C < r:
        return
    else:
        tr[r-1] = arr[C-1]
        combination(r-1,C-1)
        combination(r, C - 1)

L,C = map(int,input().split())
chars = set(list(map(str,read().split())))
arr = []
for char in chars:
    arr.append(alphabet.index(char))
arr.sort()
r = L
res = []
tr = [0]*L
combination(r,C)
for nums in res:
    char = []
    print(nums)
    for num in nums:
        char.append(alphabet[num])
    char = set(char)
    print(char)
    a = char & aeiou
    print(a)
    if len(char)-len(a) >= 2 and len(a) >= 1:
        print(''.join(char))