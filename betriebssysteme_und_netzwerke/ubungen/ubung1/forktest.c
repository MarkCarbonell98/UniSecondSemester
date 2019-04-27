#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

int main() {
    int i, j;
    pid_t pid;

    pid = fork();
    if(pid == 0) {
        /*
            Kindprozess
        */

        for(j = 0; j < 10; j++) {
                printf("Kindprozess: %d (pid: %d)\n", j, getpid());
                sleep(1); //process sleeps and goes back to the parent process
        }
        exit(0); //programm terminated 
    } else if(pid > 0) {
        // elternprozess
        // pid = ID des kindprozesses
        // getpid gibt eigene PID zuruck

        for(i = 0; i < 10; i++) {
            printf("Elternprozess: %d (pid: %d)\n", i, getpid());
            sleep(1); // process sleeps and goes back to the child process before resuming execution
        }
    } else {
        // negative value, error ocurred
        fprintf(stderr, "Fehler");
        exit(1);
    }
    return 0;
}