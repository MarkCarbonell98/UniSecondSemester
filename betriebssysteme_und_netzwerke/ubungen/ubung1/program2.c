// program 2
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

int main(int argc, char* argv[]) {
    int i = 0;
    printf("first fork pid = %d, i = %d \n", getpid(), i); //parent fork runs first
    if(fork() != 0) { // is it parent process ?
        i += 2;
        printf("second pid = %d, i = %d \n",getpid(), i);
    }
    if (fork() == 0) { // is it child process ?
        i -= 1;
        printf("thrith pid = %d, i = %d \n",getpid(), i);
    }
    if (fork() != 0) { // is it parent process ?
        i -= 1;
        printf("fourth pid = %d, i = %d \n", getpid(), i);
    }
    if (fork() * i == 0) { // is it child process ?
        fork();
        printf("fifth pid = %d, i = %d \n", getpid(), i);
    }
    exit(0);
    return 0;
}