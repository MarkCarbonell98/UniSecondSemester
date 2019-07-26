from socket import *
serverPort = 7
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The TCP server is ready to receive!")

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048)
    print("The message received by the server: ", message, addr)
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage)
    print("The message send by the server: ", modifiedMessage)
    connectionSocket.close()