// program 2
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

int main(int argc, char* argv[]) {
    int i = 0;
    if(fork() != 0) { // is it parent process ?
        i += 2;
        printf("parent process actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i); 
    }
    if (fork() == 0) { // is it child process ?
        i -= 1;
        printf("child process actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i); 
    }
    if (fork() != 0) { // is it parent process ?
        i -= 1;
        printf("parent process actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i); 
    }
    if (fork() * i == 0) { // is it child process ?
        fork();
        printf(" child process before 3 levels of nesting actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i); 
    }
    exit(0);
    return 0;
}