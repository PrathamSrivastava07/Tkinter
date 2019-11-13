from tkinter import *
#window built/ interpreter bangya
win=Tk()

#sIZE wINDOW KA
win.geometry("500x500+120+120")

#title window ka
win.title('Gui include name password')
#frame=Frame(win ,width=300 ,height=300)
#frame.grid()

##Entry
Name = Label(win, text='Name')
Age = Label(win, text='Age')
Bloodgroup = Label(win, text="Blood Group")
Disease = Label(win, text='Disease (if any}')
entry1 = Entry(win)
entry2 = Entry(win)
entry3 = Entry(win)
entry4 = Entry(win)
check = Checkbutton(win, text='Agree to T&C.')
Name.grid(row=0, column=0)
entry1.grid(row=0, column=1)
Age.grid(row=1, column=0)
entry2.grid(row=1, column=1)
Bloodgroup.grid(row=2, column=0)
entry3.grid(row=2, column=1)
Disease.grid(row=3, column=0)
entry4.grid(row=3, column=1)
check.grid(columnspan=5)












win.mainloop()