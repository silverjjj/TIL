
T = int(input())
for j in range(T):
    word = input()
    print(f"#{j + 1}",end = " ")
    if 3 <= len(word) <= 10:
        for i in range(len(word)//2):
            if word[i] == word[-1-i]:
                is_palindrome = 1
                break
            else:
                is_palindrome = 0
                break
        print(is_palindrome)
    else:
        0

