#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
//program 1
int main(int argc, char* argv[]) {
    int i = 0;
    pid_t pid = fork();
    if(fork() != 0) i++,printf("after first i++ (fork() != 0) pid = %d, i = %d \n\n",pid, i); //passing from 
    if(i != 0) {
        printf(" before fork(), (i != 0) pid = %d, i = %d \n\n",pid, i);
        fork();
        printf(" after fork(), (i != 0) pid = %d, i = %d \n\n",pid, i); 
    }
    if(fork() != 0 || i != 0) i++, printf("after last i++ (fork() != 0 || i != 0) pid = %d, i = %d \n\n",pid, i);
    if(fork() == 0 && i == 0) {
        printf(" before fork(), (fork() == 0 && i == 0) pid = %d, i = %d \n\n",pid, i);
        fork();
        printf(" after fork(), (fork() == 0 && i == 0) pid = %d, i = %d \n\n",pid, i); 
    }
    return 0;
}

