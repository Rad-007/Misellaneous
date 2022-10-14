import cv2

import time
import win32gui, win32con

def minimizewindOw():

    window=win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)



passowrd="IAMOFFICER"

def cctv():
    video=cv2.VideoCapture(0)
    video.set(3,640)
    video.set(4,480)
    width=video.get(3)

    height=video.get(4)

    print("Video resolution is a set to ", width, 'x',height)
    print("Help-- \n1.Press esc key to exit .n2\ .Press m to minimize ")
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    date_time=time.strftime("recording %H-%M-%d -%m -%y")
    output=cv2.VideoWriter('footages/'+date_time+'.mp4',fourcc,20.0,(640,480))


    while video.isOpened():
        check,frame=video.read()
        if check==True:
            frame =cv2.flip(frame,1)



            t=time.ctime()
            cv2.rectangle(frame,(5,5,100,20),(255,255,255),cv2.FILLED)
            cv2.putText(frame,'Camera 1',(20,20),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)
            cv2.putText(frame,t,(420,460),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)
            cv2.imshow('CCTV Camera',frame)
            output.write(frame)
            if cv2.waitKey(1)==27:
                print("Video Footagesaved in current directory ")
                break
            elif cv2.waitKey(1) ==ord('m'):
                minimizewindOw()
            
        
        else:
            print("Can't open camera")
            break
    
    video.release()
    output.release()
    cv2.destroyAllWindow()

print("Software CCTV")
ask=input("Do you want to open cctv[yes / no]:")

pas=0

if ask=='yes':

    pas=input("Enter password:")
    if pas==passowrd:
            cctv()
    else:
        print("Wrong Password")

    
        
else:
    print("bye")
    exit









