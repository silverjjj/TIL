import tkinter
# Create instance
win = tkinter.Tk()

# Add a title
win.title('윈도우생성하기')
lbl = tkinter.Label(win, text = "hello world")
lbl.pack()
'''
lbl - 변수명(객체instance)
Label - 클래스명
win - 소속지정(상위 윈도우)
text - Label widget의 옵션 (여러개 있음..)
'''
lbl.config(text = "안녕 파이썬")     # 변경
lbl2 = tkinter.Label(win, text = "Hello world~", bg = 'red', fg = 'white')  # bg = background ,fg = 글자색
lbl2.pack(fill = 'x')
# ==============
# Start GUI
# ==============
win.mainloop()




'''

<Label widget>
text 레이블에 표시할 문자열
anchor - 할당공간내에서 표시위치
justify - 문자열 정렬방식

모양/색상관련
width - 너비
height - 높이
relief - 테두리 모양
bd - 테두리 두께
bg(background) - 배경색상
fg(foreground) - 문자열 색상

상태관련
state - 상태
activebackground - active상태일때 배경색상
activeforeground

focus and highlight
takefocus - 포커스를 받을지 여부
highlightcolor - 선택되었을때 보더색상
highlightbackground - 선택되지 않았을때 보더색상
highlightthickness - 선택되었을 때 보더 두께
'''