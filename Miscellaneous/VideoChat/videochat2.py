from cgitb import text
from urllib import request
from vidstream import *

import tkinter as tk
import socket

import threading

import requests


local_ip_address=socket.gethostbyname(socket.gethostname())

#public_ip_address=requests.get("https://api.ipify.org").text



#server=StreamingServer('192.168.29.185',9999)


server=StreamingServer(local_ip_address,7777)
reciever=AudioReceiver(local_ip_address,6666)

def start_listening():
    t1=threading.Thread(target=server.start_server)
    t2=threading.Thread(target=reciever.start_server)

    t1.start()
    t2.start()


def start_camera_stream():
    camera_client=CameraClient(text_target_ip.get(1.0,'end-1c'),9999)
    t3=threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client=ScreenShareClient(text_target_ip.get(1.0,'end-1c'),9999)
    t4=threading.Thread(target=screen_client.start_stream)
    t4.start()


def start_audio_stream():
    audio_client=AudioSender(text_target_ip.get(1.0,'end-1c'),8888)
    t5=threading.Thread(target=audio_client.start_stream)
    t5.start()
















    




#GUI


window=tk.Tk()

window.title("Hipe")

window.geometry('300x200')

label_target_ip=tk.Label(window,text="Target IP:")
label_target_ip.pack()

text_target_ip=tk.Text(window,height=1)
text_target_ip.pack()

phone=tk.Button(window,text="Incoming",width=50,command=start_listening)
phone.pack(anchor=tk.CENTER,expand=True)

video=tk.Button(window,text="Camera",width=50,command=start_camera_stream)
video.pack(anchor=tk.CENTER,expand=True)

screen_share=tk.Button(window,text="Screen Share",width=50,command=start_screen_sharing)
screen_share.pack(anchor=tk.CENTER,expand=True)


audio=tk.Button(window,text="Audio",width=50,command=start_audio_stream)
audio.pack(anchor=tk.CENTER,expand=True)


window.mainloop()


 

