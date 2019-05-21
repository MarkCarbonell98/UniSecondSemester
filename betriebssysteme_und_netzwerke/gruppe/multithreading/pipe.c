#include <unistd.h>


char * read_from_file();
int malloc_block = 1024;
struct stat f_struct;
struct stat f_struct2;
int fd[2];
int main(int argc, char const *argv[])
{
    if(fork() == 0) {
        char c;
        char * read_text = (char *) malloc(malloc_block);
        printf("The file output end is %i \n", fd[1]);
        fstat(fd[0], &f_struct);
        printf("inode of fd[0] %li \n", f_struct.st_ino);
        fstat(fd[1], &f_struct2);
        printf("inode of fd[1] %li \n", f_struct2.st_ino);
        close(fd[1]);
        int nbytes;
        nbytes = read(fd[0], &c, 1);
        printf("nbytes %i \n", nbytes);

        *(read_text) = c;
        int i = 0;
        while(nbytes > 0) {
            i++;
            nbytes = read(fd[0], &c, 1);
            *(read_text + i) = c;
            if(strlen(read_text) + 1 == malloc_usable_size(read_text)) {
                // read_text 
            }
        }

        // char * start = read_text;
        // char * end = read_text + strlen(read_text) -1;
        // char temp;
        // while(end>start)

        // }
        // free(read_text);
    /* code */
    return 0;
}

