# #메시지
# from tkinter import *
# win = Tk()
# lbl = Message(win, text = "여러분 오랜만 입니다.\
#                 모두 잘 지내십니까 ??")
# lbl['font'] = "굴림체 15 bold"
#
# lbl.pack()
# lbl.mainloop()


# LabelFrame
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
# 응용프로그램에 버튼을 표시하는데 사용(특정명령 수행)
# 버튼에 함수를 연결시켜 호출이 가능능
#버튼예제

# from tkinter import *
# from tkinter import messagebox as m
#
# def btn_click():
#     lbl['text'] = 'hace a good day~'
#     m.showinfo('인사완료','인사를 마쳤습니다.')
#
# win=Tk()
# win.geometry("300x60")
# lbl = Label(win, text="안녕하세요 파이썬~", font="HY헤드라인M 20")
# lbl.pack()
#
# btn = Button(win, text="눌러주세요", command=btn_click, bg='red', fg='white')
# btn.pack(fill='x')

# 메시지박스 모듈
#
# from tkinter import *
# from tkinter import messagebox as m     # messagebox를 m으로 사용한다.
# window = Tk()
# window.title("메시지박스 테스트")
# window.geometry('350x200')
# def clicked():
#     m.showinfo('저장확인', '저장되었습니다.')
#     m.showwarning('용량부족','저장공간이 부족합니다.')
#     m.showerror('에러발생','에러가 발생했습니다. 종료합니다')
#     res = m.askquestion('저장확인','정말 덮어쓰시겠습니까?')
#     res = m.askyesno('종료확인','정말 종료하시겠습니까?')
#     res = m.askyesnocancel('Message title', 'Message content')
#     res = m.askokcancel('Message title','Message content')
#     res = m.askretrycancel('Message title','Message content')
# btn = Button(window, text = 'Click here', command = clicked)
# btn.grid(column = 0,row = 0)
# window.mainloop()


# Menu
