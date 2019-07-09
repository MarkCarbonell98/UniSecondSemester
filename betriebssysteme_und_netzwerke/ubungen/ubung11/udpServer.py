from socket import *

serverName = "127.0.0.1"
serverPort = 7
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((serverName, serverPort))
print("Udp server is to receive data!")

while True:
    message, clientAdress = serverSocket.recvfrom(2048)
    print("the client send the message: ", message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAdress)
