import socket

TCP_IP = '127.2.3.4'  
TCP_PORT = 52158        
run = True
jobs = 3
data = b''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
#I was having issues with using the with keyword
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    


HASC = False
#HASC2 = False
while(run):
    if not HASC:
        print("Looking for seekers...\n")
        s.listen()
        print("Found seeker!\nAwaiting confirmation...\n")
        conn, addr = s.accept()
        data =b''
        HASC = True
    #This was me trying to allow 2 connections at once (assigning tasks)
    #to 2 seekers. I dont know how any of this works
    #elif not HASC2:
    #    conn2, addr2 = s.accept()
    #    HASC2 = True

    conn.send(b'Here is a job')
    while True:
            #data = conn.recv(1024)
            #if not data:
            #    break
            #conn.send(b'Here is a job')
            data = conn.recv(1024)
            #conn.send(b'close')
            if data == b'No':
                print("Job refused :(")
                #conn.close()
                #HASC = False
                break
            else:
                conn.recv(1024)
                print("Job Complete")
                jobs-=1
                break
    if jobs <=0:
        conn.send(b'T')
        #conn.close()
        run = False
            
            
