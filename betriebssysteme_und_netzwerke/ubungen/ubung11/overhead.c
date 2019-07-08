#include "netdb.h"
#include "netinet/in.h"
#include "stdlib.h"
#include "sys/socket.h"
#include "sys/types.h"

#define MAX 80
#define PORT 7
#define SA struct socketAddress

int main(int argc, char const *argv[])
{
    void communicate(int socket_fd) {
        char buff[MAX];
        for(;;) {
            bzero(buff, MAX);
            read(socketAddress, buff, sizeof(buff));
        }
    }
    return 0;
}
