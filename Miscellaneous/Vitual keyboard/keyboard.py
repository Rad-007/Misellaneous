


import cv2 
import cvzone
import Hand_Tracking_Module as htm

from time import sleep

import numpy as np

from pynput.keyboard import Controller

cap=cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

detector=htm.HandDetector(detectionCon=0.8)
   
keyboard_keys=[["Q","W","E","R","T","Y","U","I","O","P"],["A","S","D","F","G","H","J","K","L"],["Z","X","C","V","B","N","M"]]


keyboard=Controller()
text=""



def draw(img,button_list):

    for button in button_list:

        x,y=button.pos
        w,h=button.size

        cvzone.cornerRect(img,(button.pos[0],button.pos[1],button.size[0],button.size[1]),20,rt=0)

        cv2.rectangle(img,button.pos,(int(x+w), int(y+h) ) ,(255,144,30), cv2.FILLED)

        cv2.putText(img,button.text,(x+20,y+65), cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
    
    return img

def transparent_layout(img,button_list):
    imgNew=np.zeros_like(img,np.uint8)

    for button in button_list:
        x,y= button.pos
        cvzone.cornerRect(imgNew,(button.pos[0],button.pos[1],button.size[0],button.size[1]),20,rt=0)

        cv2.rectangle(imgNew,button.pos, (x+button.size[0], y+button.size[1]), (250,144,30), cv2.FILLED)

        cv2.putText(imgNew,button.text,(x+20,y+65), cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)

        out=img.copy()
        alpha=0.5

        mash=imgNew.astype(bool)
        print(mash.shape)

        out[mash]=cv2.addWeighted(img,alpha,imgNew,1-alpha,0)[mash]

        return out


class Button():

    def __init__(self,pos,text, size=[85,85]):

        self.pos=pos
        self.size=size
        self.text=text


buttonList=[]


for k in range(len(keyboard_keys)):
    for x, key in enumerate(keyboard_keys[k]):
        buttonList.append(Button([100*x+50,100*k+50],key))



while True:
    success, img=cap.read()

    img=detector.findHands(img)
    lmlist,bboxinfo=detector.findPosition(img)

    img=draw(img,buttonList)

    if lmlist:
        for button in buttonList:

            x,y=button.pos
            w,h=button.size

            if x< lmlist[8][0] <x+w and y<lmlist[8][1] <y+h:
                cv2.rectangle(img,(x-5,y-5),(x+w+5,y+h+5),(0,255,255),cv2.FILLED)
                cv2.putText(img,button.text,(x+20,y+65),cv2.FOT_HERSHEY_PLAIN,4,(0,0),4)

                l,_=detector.findDistance(8,12,img,draw=False)
                print(l)

                if l<30:
                    keyboard.press(button.text)
                    cv2.rectangle(img,button,(x+w,y+h),(0,255,0),cv2.FILLED)
                    cv2.putText(img,button.text,(x+20,y+65),cv2.FOT_HERSHEY_PLAIN,4,(0,0),4)
                    text+=button.text
                    sleep(0.15)



    cv2.rectangle(img,(25,350),(700,450),(255,255,255),cv2.FILLED)
    cv2.putText(img,text,(60,425),cv2.FONT_HERSHEY_PLAIN,4,(0,0),4)

    cv2.imshow("output",img)
    cv2.waitKey(1)





