from tkinter import*
import calendar
def showcalendar():
    win = Tk()
    win.title('Calendar')
    win.geometry('550x600')
    fetch_year = int(year_field.get())
    Cal_content = calendar.calendar(fetch_year)
    Cal_year = Label(win,text='Cal_content',font='Consolas 10 bold')
    Cal_year.grid(row=5,column=1,padx=20)





    win.mainloop()
#DriverCode
if __name__=='__main__':
    root = Tk()
    root.config(background='Blue')
    root.title('CALENDAR')
    root.geometry('250x150')
    cal = Label(root,text='Calendar',bg='Red',font=('times',28,'bold'))
    year = Label(root,text='Enter year')
    year_field = Entry(root)

    btn = Button(root,text='Show',bd=6,background='blue',
                activebackground='green', foreground='white', command=showcalendar)
    btn.grid(row=4,column=1)

    btn2 = Button(root,text='Exit',bd=6,background='blue',
                activebackground='green', foreground='white', command=root.destroy)
    btn2.grid(row=5,column=1)







    root.mainloop
    