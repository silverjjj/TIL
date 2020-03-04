# #메시지
# from tkinter import *
# win = Tk()
# lbl = Message(win, text = "여러분 오랜만 입니다.\
#                 모두 잘 지내십니까 ??")
# lbl['font'] = "굴림체 15 bold"
#
# lbl.pack()
# lbl.mainloop()

# #LabelFrame
# from tkinter import *
# win = Tk()
#
# lframe = LabelFrame(win, text = "이름", padx=5, pady = 5)
# lframe.pack(padx = 10, pady = 10)
#
# e = Entry(lframe)     # 프레임 안에 앤트리가 들어가있움움
# e.pack()
# win.mainloop()



# Button
# 버튼예제

from tkinter import *
from tkinter import messagebox as m

def btn_click():
    lbl['text'] = 'hane a good day~'
    m.showinfo('인사완료','인사를 마쳤습니다.')

win = Tk()
win.geometry("300x60")
lbl = Label(win, text = "안녕하세요 파이썬~", font = "HY헤드라인M 20")
lbl.pack()

btn = Button(win, text = "눌러주세요", command = btn_click, bg ='red', fg = 'white')
btn.pack(fill = 'x')