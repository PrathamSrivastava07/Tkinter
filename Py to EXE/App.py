from tkinter import *
#window built/ interpreter bangya
win=Tk()

#title window ka
win.title('GUI')


def hi(event):
    lb=Label(win, text='Left Button is pressed').pack()

def hi1(event):
    lb2=Label(win, text='Right Button is pressed').pack()

def hi2(event):
    lb1=Label(win, text='Wheel Button is pressed').pack()

'''btn = Tk.Button(win, text = "Click Me!")
btn.bind("<Button-1>", hi) # 'bind' takes 2 parameters 1st is 'event' 2nd is 'function'
btn.pack()'''

btn= Button(win, text='Click')
btn.bind('<Button-1>',hi) #binding mouse button
btn.bind('<Button-3>',hi1)
btn.bind('<Button-2>',hi2)
btn.pack()



win.mainloop()
