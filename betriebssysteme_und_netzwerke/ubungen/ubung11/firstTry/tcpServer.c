#include "netdb.h"
#include "netinet/in.h"
#include "stdlib.h"
#include "string.h"
#include "sys/socket.h"
#include "sys/types.h"

#define MAX 80
#define PORT 7
#define SA struct sockaddr;

void hold_connection(int socket_fd) {
    char buffer[MAX];
    int n;
    // infine loop 
    for(;;) {
        bzero(buffer, MAX);
        read(socket_fd, buffer, sizeof(buffer));

        printf("From client %s\t to client: ", buffer);
        
    }
}