from tkinter import *


def donate():
    win.quit()
    root =Tk()


    root.geometry("500x500")

#title rootdow ka
    root.title('Registration')
#frame=Frame(root ,width=300 ,height=300)
#frame.grid()


    Name = Label(root, text='Name')
    Age = Label(root, text='Age')
    Bloodgroup = Label(root, text="Blood Group")
    Disease = Label(root, text='Disease (if any}')
    entry1 = Entry(root)
    entry2 = Entry(root)
    entry3 = Entry(root)
    entry4 = Entry(root)
    check = Checkbutton(root, text='Agree to T&C.')
    Name.grid(row=0, column=0)
    entry1.grid(row=0, column=1)
    Age.grid(row=1, column=0)
    entry2.grid(row=1, column=1)
    Bloodgroup.grid(row=2, column=0)
    entry3.grid(row=2, column=1)
    Disease.grid(row=3, column=0)
    entry4.grid(row=3, column=1)
    check.grid(columnspan=5)
    br = Button(root, text="SUBMIT", bg='Light Yellow', fg='Black')
    br.grid(row=5,column=8)


    root.mainloop()




win = Tk()
win.geometry("1100x500")
c=win.quit()
win.title('Blood Donatiom')
frame=Frame(win ,width=300 ,height=300)
photo = PhotoImage(file="preview.png")
#photo1 = PhotoImage(file="canstockphoto53299191.png")
button2= Label(frame, text='SAVE blood',bg='White', fg='Red', image=photo,font=5)
label = Label(win, text="Choose Option",bg='Red')
#button3= Label(frame, text='SAVE blood',bg='Black', fg='Red', image=photo,font=7)
b1 = Button(win, text="Donate", bg='Light pink', fg='Black', activebackground='white', command= donate)
b2 = Button(win, text="Show",bg='Light pink', fg='Black')

# This is where b1 is placed inside b2 with in_ option
b1.place(in_=button2, relx=0.4, rely=0.4, anchor=CENTER)
b2.place(in_=button2, relx=0.6, rely=0.4, anchor=CENTER)

frame.pack()
label.place(in_=button2, relx=0.5, rely=0.2, anchor=CENTER)
#label.pack(fill=X)
button2.pack(side=LEFT)
#button3.pack(side=RIGHT)
win.mainloop()
