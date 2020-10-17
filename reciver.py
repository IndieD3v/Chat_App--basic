import socket

c = socket.socket()
c.connect(("localhost", 4000))

name = input("Enter Your Name: ")
c.send(name.encode())

for i in range(3):

    msgs = input("Enter message: ")
    me = c.send(msgs.encode())

    sender = c.recv(1024).decode()
    print(sender)

    if(msgs == "quit"):
        break

c.close()