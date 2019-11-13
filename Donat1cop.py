def donate():
    root =Tk()


    root.geometry("500x500+120+120")

#title rootdow ka
    root.title('Gui include name password')
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












    root.mainloop()