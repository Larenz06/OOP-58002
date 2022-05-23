from tkinter import *
window = Tk()
window.geometry("400x300+20+10")
window.title('Final Exam')


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text=("Enter the first number:"))
        self.txtfld1 = Entry()
        self.txtfld1.place(x=200, y=70)
        self.txtfld1.place(width=100, height=20)
        self.lbl2 = Label(win, text=("Enter the second number:"))
        self.txtfld2 = Entry()
        self.txtfld2.place(x=200, y=100)
        self.txtfld2.place(width=100, height=20)
        self.lbl3 = Label(win, text=("Enter the third number:"))
        self.txtfld3 = Entry()
        self.txtfld3.place(x=200, y=130)
        self.txtfld3.place(width=100, height=20)
        self.lbl1.place(x=30, y=70)
        self.lbl2.place(x=30, y=100)
        self.lbl3.place(x=30, y=130)
        self.lbl4 = Label(win, text=("The smallest number among the three is:"))
        self.lbl4.place(x=30, y=160)
        self.txtfld4 = Entry()
        self.txtfld4.place(x=200, y=190)
        self.txtfld4.place(width=100, height=20)
        self.btn1 = Button(window, text="Show", command=self.main)
        self.btn1.place(x=30, y=190)

    def main(self):
        self.txtfld4.delete(0, 'end')
        L = []
        num1 = int(self.txtfld1.get())
        L.append(num1)
        num2 = int(self.txtfld2.get())
        L.append(num2)
        num3 = int(self.txtfld3.get())
        L.append(num3)
        answer = str(min(L))
        self.txtfld4.insert(END,answer)

mywin = MyWindow(window)

window.mainloop()




