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
    int socket_fp;
    char * message = "Servus!";
    struct sockaddr_in client_address, server_address;
    char * buffer[MAXLINE];

    if((socket_fp = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&client_address, 0, sizeof(client_address));
    memset(&server_address, 0, sizeof(server_address));

    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = INADDR_ANY;
    server_address.sin_port = htons(PORT);

    if(bind(socket_fp, (const struct sockaddr *)&server_address, sizeof(server_address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    int message_length, last_index;
    last_index = recvfrom(socket_fp, (char *) buffer, MAXLINE,
                MSG_WAITALL, (struct sockaddr *)&client_address, &message_length);

    buffer[last_index] = '\0';
    printf("Client: %s\n", buffer);
    sendto(socket_fp, (const char *) message, strlen(message), MSG_CONFIRM, (const struct sockaddr *) &client_address, message_length);

    printf("The message '%s' was sent \n", message);

    return 0;
}

