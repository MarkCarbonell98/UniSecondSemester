#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <string.h>

char * strrev(char * str) {
        char c, * front, * back;
        if(!str || !*str) return str;
        for(front = str, back=str+strlen(str) -1; front < back; front++, back--) {
                c = *front; *front = *back, *back = c;
        }
        return str;
}

int main(int argc, char ** argv) {
        int     fd[2], nbytes;
        pid_t   childpid;
        char    string[100];
        char    readbuffer[100];
        printf("Insert a string to write to: \n");
        fgets(string, 100, stdin);
        pipe(fd);
        
        if((childpid = fork()) == -1)
        {
                perror("fork");
                exit(1);
        }

        if(childpid == 0)
        {
                /* Child process closes up input side of pipe */
                close(fd[0]);

                /* Send "string" through the output side of pipe */
                write(fd[1], string, (strlen(string)+1));
                exit(0);
        }
        else
        {
                /* Parent process closes up output side of pipe */
                close(fd[1]);

                /* Read in a string from the pipe */
                nbytes = read(fd[0], readbuffer, sizeof(readbuffer));
                
                char * copy = readbuffer;
                strrev(copy);                
                

                printf("Reverse string: %s \n", copy);
        }

        return(0);
}