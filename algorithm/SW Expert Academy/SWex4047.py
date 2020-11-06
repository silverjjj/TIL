# T = int(input())
# for tc in range(1, T + 1):
#     bases = str(input())
#     base = []
#     for i in bases:
#         base.append(i)
#     h_num = d_num = s_num = c_num = 0
#     card = []
#     for i in range(0, len(bases), 3):
#         card.append(bases[i:i + 3])
#     a = list(set(card))
#
#     if len(a) == len(card):
#         for i in range(len(a)):
#             if a[i][0] == 'H':
#                 h_num += 1
#             elif a[i][0] == 'D':
#                 d_num += 1
#             elif a[i][0] == 'S':
#                 s_num += 1
#             elif a[i][0] == 'C':
#                 c_num += 1
#         print("#{} {} {} {} {}".format(tc, 13 - s_num, 13 - d_num, 13 - h_num, 13 - c_num))
#     else:
#         print(f"#{tc} " + "ERROR")

# T = int(input())
# for tc in range(1,T+1):
#     case = input()
#     s_cnt = d_cnt = h_cnt = c_cnt = 0
#     s = []
#     for i in range(0,len(case),3):
#         s.append(case[i:i+3])
#     for i in range(len(s)):
#         for j in range(i+1,len(s)):
#             print(s[i],s[j])
#             if s[i] == s[j]:
#                 print('#{} ERROR'.format(tc))
#                 break
#             else:
#                 if s[i+3] == 'S':
#                     s_cnt +=1
#                 elif s[i+3] == 'H':
#                     h_cnt +=1
#                 elif s[i+3] == 'D':
#                     d_cnt +=1
#                 elif s[i+3] == 'C':
#                     c_cnt +=1
#             print('#{} {} {} {} {}'.format(tc,13-s_cnt, 13-d_cnt, 13-h_cnt, 13-c_cnt))
