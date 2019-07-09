from socket import *
import time

serverName = 'localhost'
serverPort = 7
repetitions = 1000

start = time.time()
while repetitions >= 0:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = "Hello from the UDP client!"
    clientSocket.sendto(str.encode(message), (serverName, serverPort))
    print(f"The message send is: {message}")

    # get response
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("The message received is: ", modifiedMessage.decode())
    clientSocket.close()
    repetitions -= 1
end = time.time()
print("Time elapsed: ", end - start, " seconds")
