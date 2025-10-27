from tkinter import*
win = Tk()
win.geometry('300x300')
calendar = Label(win,text='Calendar')
calendar.grid(row=1,column=1)

year = Label(win,text='Year')
year.grid(row=2,column=1)

year_field=Entry(win)
year_field.grid(row=3,column=1)

btn = Button(win,text='Show',bd=6,background='blue',
                activebackground='green', foreground='white', command=None)
btn.grid(row=4,column=1)

btn2 = Button(win,text='Exit',bd=6,background='blue',
                activebackground='green', foreground='white', command=win.destroy)
btn2.grid(row=5,column=1)

win.mainloop()
