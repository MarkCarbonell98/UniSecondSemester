#include "stdio.h"
#include "unistd.h"

int main(void) {
}

int main(int argc, char const *argv[])
{
    // aufgabe 1
    while(1) {
        read_command("some_command", "some parameters");
        if(fork() > 0) {
            waitpid(-1, NULL, 0)
            // or wait(NULL)
        } else {
            execve(command, parameters, NULL)
        }
    }
    // aufgabe 2
    printf("Main program started\n");
    char* argv[] = { "jim", "jams", NULL };
    char* envp[] = { "some", "environment", NULL };
    execve("./sub", argv, envp) == -1;
    perror("Could not execve");

    // aufgabe 3
    // open the file, if it doesnt exist then create one
    int fd = open("some_file.txt", O_WRONGLY | O_CREAT);
    //set the file descriptor of the opened file to 1 => fd of stdout
    //ie the pointer at file_struct at index 1 points at the opened file
    // openend -> the output to the stdin is now redirected to opened file
    int status = dup2(fd,1)
    // file descriptors remain open by default across an exec calling, ls will result
    // this will print the output of ls into the open file, which points to the standard output 
    execl("/bin/ls", "/bin/ls", "/home/ek/Downloads", NULL)
    //same as ls /home/ek/Downloads > some_file.txt
    return 0;
}
