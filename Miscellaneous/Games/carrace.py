
import pygame

import time
import random

import os
pygame.init()






pygame.init() 
#color code in RGB form
gray=(60,60,60)
#color code in RGB form
black=(255,0,0) 
#set width & height of the display
display=pygame.display.set_mode((900,600))
#set name of the game window
pygame.display.set_caption("Racing game built with python")  



#load car image

car_img=pygame.image.load("images/car4.png")

background=pygame.image.load("images/background.png")



car_width=23


def policecar(police_startx,police_starty,police):

    if police==0:
       police_come=pygame.image.load("images/car2.png")

    
    if police==1:
        police_come=pygame.image.load("images/car3.png")
    
    
    police_come=pygame.image.load("images/car1.png") 
    display.blit(police_come,(police_startx,police_starty))



def back_ground():


    display.blit(background,(0,0))       



def message_display(text):

    large_text=pygame.font.FONT("freesansbold.ttf",80)

    textsurf,textrect=text_object(text,large_text)

    textrect.center=((400),(300))

    display.blit(textsurf,textrect)
    
    pygame.display.update()

    time.sleep(3)

    loop()

def text_object(text,font):

    text_surface=font.render(text,True,black)  
    return (text_surface,text_surface.get_rect() )


def crash():
    message_display("GAME  OVER!!!")



def car(x,y):

    display.blit(car_img,(x,y))


def loop():


    x=560
    y=300

    x_change=0

    y_change=0


    policecar_speed=0

    police=0

    police_startx=random.randrange(130,700-car_width)

    police_starty=-600

    police_width=23

    police_height=47


    bumped=False

    while not bumped:

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()

                quit()


            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:

                    x_change=-1

                if event.key==pygame.K_RIGHT:
                    x_change=1


                
            if event.type==pygame.KEYUP:
                x_change=0

        x+=x_change

        display.fill(gray)

        back_ground()

        police_starty-=(policecar_speed/1.2)

        policecar(police_startx,police_starty,police)

        police_starty+=policecar_speed

        car(x,y)

        if x<130 or x>700-car_width:

            crash()

        if police_starty>600:     
            #only one car will cross the road in one time
            police_starty=0-police_height 
            #then other car will come
            police_startx=random.randrange(130,(1000-300)) 

            police=random.randrange(0,2)

        if y<police_starty+police_height:
            if x>police_startx and x<police_startx+police_width or x+car_width >police_startx and x+car_width< police_startx+police_width:
                crash()
        

        pygame.display.update()

loop()

pygame.quit()

quit()







