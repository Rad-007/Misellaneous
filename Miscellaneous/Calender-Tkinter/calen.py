
from tokenize import String
from turtle import exitonclick
import calendar

from tkinter import *

yearint=0

def showCalender1():

    global year

    gui=Tk()

    gui.config(background="white")

    gui.title("Calendar")

    gui.geometry("550x600")

    

    

    gui_content=calendar.calendar(year+1)

    calYear=Label(gui,text=gui_content,font="Consolas 10 bold")

    calYear.grid(row=5,column=1,padx=20)



isClickedNxt=False  
isClickedPre=False  


def showCalender(y):

    
    global isClickedNxt, isClickedPre

    g=Tk()

    g.config(background="white")

    g.title("Calendar")

    g.geometry("550x600")

    

    

    g_content=calendar.calendar(y)

    calYear=Label(g,text=g_content,font="Consolas 10 bold")

    calYear.grid(row=5,column=1,padx=20)


    
    #cal(year)

    
    
   
    nxt=Button(g,text="Next",bd=0,bg="#fff",command=lambda: showCalender(y+1))
    #g.destroy()
    
    nxt.place(x=400,y=550)
    isClickedNxt=True

    


    pre=Button(g,text="Previous",bd=0,bg="#fff",command=lambda: showCalender(y-1))
    pre.place(x=100,y=550)
    
    isClickedPre=True

   

    
    g.mainloop()
    



'''
#Driver code
if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calender")
    new.geometry("250x250")
    cal = Label(new, text="Calender",bg='grey',font=("times", 28, "bold"))
    #Label for enter year
    #year = Label(new, text="Enter year", bg='dark grey')
    #text box for year input
    year_field=StringVar()
    y=Entry(new,text=year_field,width=10,font="arial 15")
    #y.place(x=100,y=100)
    

    if year_field.get():
        yearint=int(year_field.get())
    else:
        yearint=2022

    
    button = Button(new, text='Show Calender',fg='Black',bg='Blue',command=lambda: showCalender(yearint))

    #adjusting widgets in position
    cal.grid(row=1, column=1)
    #year.grid(row=2, column=1)
    #y.grid(row=3, column=1)
    button.grid(row=4, column=1)
    exit = Button(new, text='Exit',fg='Black',bg='Blue',command=new.destroy)
    exit.grid(row=6, column=1)
    new.mainloop()

'''

showCalender(2022)