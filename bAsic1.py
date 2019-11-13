from tkinter import *
#window built/ interpreter bangya
win=Tk()

#title window ka
win.title('GUI')

#LAbel    Note: Fill function Label par kaam krega
LaBel= Label(win , text='Basic label',bg='Red')

LaBel.pack(fill=X)
#FRAMES
frame=Frame(win)
'''Button Creation'''
button1= Button(frame, text='Button1',bg='Cyan', fg='Red')
button2= Button(frame, text='Button2',bg='Violet', fg='Red')
button3= Button(frame, text='Button3 with fill',bg='Violet', fg='Red')

button1.pack()
button2.pack()
button3.pack()
frame.pack(side=TOP)


'''Ye frame window ka sixe bada krta hai'''
frame1=Frame(win ,width=500,height=300)
frame1.pack()


win.mainloop()
