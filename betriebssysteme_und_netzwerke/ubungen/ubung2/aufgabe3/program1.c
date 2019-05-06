#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
//program 1
int main(int argc, char* argv[]) {
    int i = 0;
    if(fork() != 0) { // is it parent process ?
        i++;
        printf("I am the parent process actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i);
    }
    if(i != 0) { // is this a child of the parent process ?
        printf("I am a child of the parent process before fork actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i);
        printf("I am a child of the parent process after fork actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i); 
    }
    if(fork() != 0 || i != 0) { //is this a parent process inside a child process ?
        i++;
        printf("I am a parent process inside the main parent process actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i);
    }
    if(fork() == 0 && i == 0) { // is this a child process inside a children process ?
        printf(" I am the child process created inside the second parent process before fork actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i);
        fork();
        printf(" I am the child process created inside the second parent process before fork actualPid = %d, parentPid = %d, i = %d \n\n",getpid(), getppid(), i); 
    }
    exit(0);
    return 0;
}

//prozesse

/*
    
*/

