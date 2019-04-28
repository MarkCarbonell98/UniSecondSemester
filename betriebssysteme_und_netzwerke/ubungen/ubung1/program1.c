#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
//program 1
int main(int argc, char* argv[]) {
    int i = 0;
    if(fork() != 0) { // is it parent process ?
        i++;
        printf("first getpid() = %d, i = %d \n\n",getpid(), i);
    }
    if(i != 0) { // is this a child of the parent process ?
        printf("second before getpid() = %d, i = %d \n\n",getpid(), i);
        fork();
        printf("second after getpid() = %d, i = %d \n\n",getpid(), i); 
    }
    if(fork() != 0 || i != 0) { //is this a parent process inside a child process ?
        i++;
        printf("third getpid() = %d, i = %d \n\n",getpid(), i);
    }
    if(fork() == 0 && i == 0) { // is this a child process inside a children process ?
        printf(" fourth before getpid() = %d, i = %d \n\n",getpid(), i);
        fork();
        printf(" fourth after getpid() = %d, i = %d \n\n",getpid(), i); 
    }
    exit(0);
    return 0;
}

//prozesse

/*
    
*/

