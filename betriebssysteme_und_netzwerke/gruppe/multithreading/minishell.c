#include <sys/sysinfo.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <pthread.h>

int main(int argc, char const *argv[])
{
    
    if(argc == 1) {
        char * name = argv[0];
        pid_t pid = fork();
        int s = 0;
        wait(s);
        if(pid == 0) {
            printf("I am the child process and my name is %s", name);
            signal(s);
        }
        printf("I am the father process and my child %s just finished", name);
    }

    char * parameters = argv;

    while(1) {
        read_command(command, parameters);
        if(fork() != 0) {
            //
            waitpid(-1, &status, 0);
        } else {
            execve(command, parameters, 0)
        }
    }


    return 0;
}
