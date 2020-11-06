chars = input()
cnt = 1
if chars[0] == " ":
    cnt -= 1
if chars[-1] == " ":
    cnt -= 1
for num in chars:
    if num == " ":
        cnt += 1
print(cnt)