from tkinter import *
#window built/ interpreter bangya
win=Tk()

#sIZE wINDOW KA
win.geometry("500x500+120+120")

#title window ka
win.title('Gui include name password')
#frame=Frame(win ,width=300 ,height=300)
#frame.grid()

#Entry
Name= Label(win, text='Name')
Password= Label(win, text='Pass')
entry1= Entry(win)
entry2= Entry(win)
check= Checkbutton(win, text='Keep logged in')
Name.grid(row=0, column=0)
entry1.grid(row=0, column=1)
Password.grid(row=1, column=0)
entry2.grid(row=1, column=1)
check.grid(columnspan=5)

#function binding



win.mainloop()