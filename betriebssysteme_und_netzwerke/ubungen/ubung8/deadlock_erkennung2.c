#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100
#define BUFFER_SIZE 500

void printArray(int *arr, int length)
{
    int i = 0;
    printf("[ ");
    for (i = 0; i < length; i++)
    {
        if (i == length - 1)
            printf("%d", arr[i]);
        else
            printf("%d,", arr[i]);
    }
    printf(" ]\n");
}

int main(int argc, char const *argv[])
{
    if(argv[1] == NULL || argc < 2) {
        perror("No file to read was entered\n");
        exit(EXIT_SUCCESS);
    }
    const char * filename = argv[1];
    printf("The read file is %s\n", filename);
    char process_number_id = 'p', resource_number_id = 'r', vector_e_id = 'e', vector_a_id = 'a', matrix_c_id = 'C', matrix_r_id = 'R';
    char * buffer = malloc(MAX_SIZE * sizeof(char));
    size_t buffer_length = 0;
    ssize_t line_length = 0;
    int process_number = 0, resource_number = 0;
    int * vector_e = malloc(MAX_SIZE * sizeof(int));
    int * vector_a = malloc(MAX_SIZE * sizeof(int));
    int * matrix_c = malloc(MAX_SIZE * sizeof(int));
    int * matrix_r = malloc(MAX_SIZE * sizeof(int));
    FILE * fp;
    fp = fopen(filename, "r");
    char c;
    while((line_length = getline(&buffer, &buffer_length, fp)) != -1) {
        printf("The line lenght is %ld, and the line is \n %s", line_length, buffer);
        if(buffer[0] == process_number_id) {
            printf("%c", buffer[2]);
            c = buffer[2] == '0' ? 0 : c - '0';
            process_number = c;
            // for(size_t i = 2; i < line_length; i++) {
            //     if(buffer[i] != ' ' && buffer[i] != '\n') {
            //         process_number = c;
            //     }
            // }
        }
    }

    printf("The amount of processes is %d\n", process_number);
    free(vector_e);
    free(vector_a);
    free(matrix_c);
    free(matrix_r);
    free(buffer);
    return 0;
}
