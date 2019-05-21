#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <unistd.h>

int main(void) {
    int pipe_c[2];
    pipe(pipe_c);
    if(fork() == 0) {
        dup2(pipe_c[1], 1);
        close(pipe_c[0]);
        execlp("who", "who", NULL);
    } else if (fork() != 0) {
        dup2(pipe_c[0], 0);
        close(pipe_c[1]);
        execlp("sort", "sort", NULL);
    }
}