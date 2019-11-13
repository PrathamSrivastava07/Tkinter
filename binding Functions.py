from tkinter import *
#window built/ interpreter bangya
win=Tk()

#title window ka
win.title('GUI')

def hi(event):
    lb=Label(win, text='Button is pressed').pack()

'''btn = Tk.Button(win, text = "Click Me!")
btn.bind("<Button-1>", hi) # 'bind' takes 2 parameters 1st is 'event' 2nd is 'function'
btn.pack()'''

btn= Button(win, text='Click')
btn.bind('<Button-1>',hi) #binding mouse button
btn.pack()



win.mainloop()
