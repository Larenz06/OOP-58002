from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Enter your fullname:', fg='Red')
        self.t1=Entry()
        self.t1.place(x=150, y=70)
        self.t1.place(width=150, height=20)
        self.t2 = Entry()
        self.t2.place(x=200, y=100)
        self.lbl1.place(x=30, y=70)
        self.btn1 = Button(win,text='Click to Display your fullname', fg='Red', font="Times 9")
        self.btn1.place(x=30, y=100)
        self.t2.place(width=150, height=20)




window = Tk()
mywin = MyWindow(window)
window.title('Midterm Exam')
window.geometry("400x300+10+10")
window.mainloop()