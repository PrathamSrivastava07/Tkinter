from tkinter import *

class Window:
    def _init_(self, master):
        self.button1 =Button(master, text= "Print hi", command=printmsg)
        self.button1.pack()

    def printmsg(self):
        print('HELLO')


#window built/ interpreter bangya
win= Tk()

b = Window(win)
win.geometry("500x500+120+120")

win.mainloop()