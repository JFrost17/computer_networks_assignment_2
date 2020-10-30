#No actual calculations are performed in this assignment
#The if statements are to simulate jobs being finished and or uncompleted
import socket
import time
import threading

#Default TCP IP and Port
TCP_IP = '127.2.3.4'  
TCP_PORT = 52158
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = b''
#Should we still run?
run = True

Connected = False

while run:
    #This was in an attempt to allow disconnection of client, and have it reconnect
    #afterwards. I cant get it to work. Currently this functions fine as is
    #but it doesnt hit like, any of the requirements
    try:
        data = s.recv(1024)
    except:
        s.connect((TCP_IP, TCP_PORT))
        data = s.recv(1024)
        #Connected = True

    print("Looking for job...")

    #If the job creator has no more jobs
    if data == b'T':
        run = False
        break
    ui = input("Found Job, Accept? y/n\n")

    if ui in ["y","Y"]:
        s.send(b'Yes')
        time.sleep(1)
        s.send(b'done')
        #data = s.recv(1024)
        print("Job finished")
    else:
        s.send(b'No')
        time.sleep(1)
        #data = s.recv(1024)
        #Connected = False
        print("Job refused")
    
