#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int i = 0;
    if(fork() != 0) i++;
    if(fork() == 0) fork();
    if(fork() != 0) fork();
    if (fork() *i == 0) fork();
    printf("Hi, i am the process %d and my parent is %d", getpid(), getppid());
    sleep(10);
    return 0;
}
