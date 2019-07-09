#include "stdlib.h"
#include "stdio.h"
#include "sys/socket.h"
#include "netinet/in.h"
#include "string.h"
#include "sys/types.h"
#include "arpa/inet.h"
#include "unistd.h"

#define PORT 7
#define MAXLINE 1024

int main(int argc, char const *argv[])
{
    int socket_fd;
    char buffer[MAXLINE];
    char * message = "Hello from udpclient!";
    struct sockaddr_in server_address;

    if((socket_fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed!");
        exit(EXIT_FAILURE);
    }

    memset(&server_address, 0 , sizeof(server_address));

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = INADDR_ANY;
    int last_index, message_length;

    sendto(socket_fd, (const char *) message, strlen(message), MSG_CONFIRM, (const struct sockaddr *) &server_address, sizeof(server_address));
    printf("The message %s was sent to the server!");

    message_length = recvfrom(socket_fd, (char *)buffer, MAXLINE, MSG_WAITALL, (struct sockaddr *) &server_address, &message_length);

    buffer[message_length] = '\0';
    printf("Server says: %s\n", buffer);
    close(socket_fd);
    return 0;



    return 0;
}
