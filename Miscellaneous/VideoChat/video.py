from pyfiglet import Figlet
import os

os.system("clear")

pyf=Figlet(font="puffy")

a=pyf.renderText("Video Chat App without multithreading")

b=pyf.renderText("Server")

os.system('tput setaf 3')

print(a)

import socket ,cv2, pickle, struct

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host_name=socket.gethostname()
host_ip=socket.gethostbyname(host_name)

print("Host IP:", host_ip)

port=9999

socket_adddress=(host_ip,port)

server_socket.bind(socket_adddress)

server_socket.listen(1)
print("Listening at: ",socket_adddress)


while True:
    client_socket,addr=server_socket.accept()
    print("Connected to :",  addr)
    vid=0

    if client_socket:
        vid-cv2.VideoCapture(0)

    while (vid.isOpened()):
        ret,img=vid.read()
        img_spec=pickle.dumps(img)
        message=struct.pack("Q",len(img_spec))+img_spec

        client_socket.sendall(message)

        cv2.imshow('Video from server',img)

        hey=cv2.waitKey(10)
        if hey==13:
            client_socket.close()
