

from tkinter import *

from tkinter.messagebox import showinfo

root=Tk()

y=""
x=2

player_1=[]
player_2=[]

win=[6,12,15,18,24]

def sum(l):
    s=0
    for i in l:
        s=s+i
    
    return(s)

    


def define_sign(n):
    global x,y

    global player_1, player_2

    global win

    

    if sum(player_1 ) in win :
        print("Winner is player 1")
        showinfo("Result","Player 1 is Winner")
    
    elif sum(player_2) in win :
        print("Winner is player 2")
        showinfo("Result","Player 2 is Winner")


    if n==1:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b1.config(text=y)
        x+=1


    if n==2:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b2.config(text=y)
        x+=1

    if n==3:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b3.config(text=y)
        x+=1


    if n==4:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b4.config(text=y)
        x+=1


    if n==5:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b5.config(text=y)
        x+=1

    

    if n==6:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b6.config(text=y)
        x+=1


    if n==7:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b7.config(text=y)
        x+=1



    if n==8:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b8.config(text=y)
        x+=1


    if n==9:
        if x%2==0:
            y='X'
            player_1.append(n)
        elif x%2!=0:
            y='O'
            player_2.append(n)
        
        b9.config(text=y)
        x+=1

    
    print("pLAYER 1",player_1)
    print("pLAYER 2",player_2)





l1=Label(root,text="Player 1 : X",font="times 15 ")
l1.grid(row=0,column=1)

l2=Label(root,text="Player 1 : O",font="times 15 ")
l2.grid(row=0,column=2)


b1=Button(root,width=5,height=5,command=lambda: define_sign(1) )
b1.grid(row=1,column=1)

b2=Button(root,width=5,height=5,command=lambda: define_sign(2) )
b2.grid(row=1,column=2)

b3=Button(root,width=5,height=5,command=lambda: define_sign(3) )
b3.grid(row=1,column=3)

b4=Button(root,width=5,height=5,command=lambda: define_sign(4) )
b4.grid(row=2,column=1)

b5=Button(root,width=5,height=5,command=lambda: define_sign(5) )
b5.grid(row=2,column=2)

b6=Button(root,width=5,height=5,command=lambda: define_sign(6) )
b6.grid(row=2,column=3)

b7=Button(root,width=5,height=5,command=lambda: define_sign(7) )
b7.grid(row=3,column=1)

b8=Button(root,width=5,height=5,command=lambda: define_sign(8) )
b8.grid(row=3,column=2)

b9=Button(root,width=5,height=5,command=lambda: define_sign(9) )
b9.grid(row=3,column=3)




root.mainloop()
