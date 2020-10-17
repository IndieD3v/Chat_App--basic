import socket

server = "localhost"
port = 4000

#Create Sockret
s = socket.socket()
s.bind((server, port))
s.listen(1)
print("Connecting on Port:", port)

c, addr = s.accept()

reciver_name = c.recv(1024).decode()
print("Connected To: ", reciver_name)


while True:

    sender_msg = c.recv(1024).decode()
    print(sender_msg)

    message = input("Enter Message: ")
    c.send(message.encode())

    if(message == "quit"):
        break

c.close()




