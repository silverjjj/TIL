
keyboard = {1 : [0,0], 2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],"*":[3,0],0:[3,1],'#':[3,2]}
def solution(numbers, hand):
    ans = ''
    left = (1,4,7)
    right = (3,6,9)
    cur_left = '*'; cur_right = '#'
    for number in numbers:
        if number in left:
            ans += 'L'
            cur_left = number
        elif number in right:
            ans += 'R'
            cur_right = number
        else:
            nx, ny = keyboard[number]
            rx, ry = keyboard[cur_right]
            lx, ly = keyboard[cur_left]

            if (abs(rx-nx) + abs(ry-ny)) < (abs(lx-nx) + abs(ly-ny)):
                ans += 'R'
                cur_right = number
            elif (abs(rx-nx) + abs(ry-ny)) > (abs(lx-nx) + abs(ly-ny)):
                ans += 'L'
                cur_left = number
            elif (abs(rx-nx) + abs(ry-ny)) == (abs(lx-nx) + abs(ly-ny)):
                if hand == "right":
                    ans += 'R'
                    cur_right = number
                else:
                    ans += 'L'
                    cur_left = number
    return ans

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
solution(numbers, hand)