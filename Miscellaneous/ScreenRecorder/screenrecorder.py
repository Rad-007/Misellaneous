from tkinter import*

import pyscreenrec

root=Tk()

root.geometry("400x600")
root.title("ScreenRec")

root.config(bg='#fff')

root.resizable(False,False)




rec=pyscreenrec.ScreenRecorder()

icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,icon)


def start_rec():

    file=FileName.get()
    root.iconify()
    rec.start_recording(str(file+".mp4"),5)




#background

img1=PhotoImage(file="Images/yellow.png")
Label(root,image=img1,bg="#fff").place(x=-2,y=35)


img2=PhotoImage(file="Images/blue.png")
Label(root,image=img2,bg="#fff").place(x=223,y=200)


    


def pause_rec():
    rec.pause_recording()



def resume_rec():
    rec.resume_recording()

    

def stop_rec():
    done=Button(root,text="Done",font="arial 22",bd=0)#command=start_rec)
    done.place(x=140,y=250)
    rec.stop_recording()





#heading

lbl=Label(root,text="Screen Recorder",bg="#fff",font="arial 15 bold")
lbl.pack(pady=20)

img3=PhotoImage(file="Images/recording.png")
Label(root,image=img3,bg="#fff").pack(pady=30)


#entry

FileName=StringVar()
entry=Entry(root,textvariable=FileName,width=18,font="arial 15")
entry.place(x=100,y=350)
FileName.set("New Recording")







#buttons

start=Button(root,text="Start",font="arial 22",bd=0,command=start_rec)
start.place(x=140,y=250)


img4=PhotoImage(file="Images/pause.png")
pause=Button(root,image=img4,bd=0,bg="#fff",command=pause_rec)
pause.place(x=50,y=450)

img5=PhotoImage(file="Images/resume.png")
resume=Button(root,image=img5,bd=0,bg="#fff",command=resume_rec)
resume.place(x=150,y=450)

img6=PhotoImage(file="Images/stop.png")
stop=Button(root,image=img6,bd=0,bg="#fff",command=stop_rec)
stop.place(x=250,y=450)



root.mainloop()