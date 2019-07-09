from socket import *
import time


serverName = 'localhost'
serverPort = 7
start = time.time()
repetitions = 1000
while repetitions >= 0:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    message = "Hello from the TCP client!"
    clientSocket.send(str.encode(message))
    print("TCP client received send the message: ", message)
    modifiedMessage = clientSocket.recv(2048)
    print("Received the message: ", modifiedMessage)
    clientSocket.close()
    repetitions -= 1
end = time.time()
print("Time Elapsed: ", end - start, "seconds")
