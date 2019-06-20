#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SIZE 100
#define INFINITY 2147483647

void print_array(int *arr, int length)
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

void write_line_to_vector(int * vec, char * buffer, ssize_t length) {
    int vec_index = 0;
    for (ssize_t i = 0; i < length; i++)
    {
        if (isdigit(buffer[i]))
        {
            vec[vec_index] = buffer[i] - '0';
            vec_index++;
        }
    }
}

int vec_every(int * vec, int length, int item) {
    for(int i = 0; i < length; i++) {
        if(vec[i] != item) return 0;
    }
    return 1;
}

// this function supposes that both vectors have the same length
int is_vec_smaller_or_equal(int * vec, int * matrix_vec, int length) {
    for(int i = 0; i < length; i++) {
        if(!(matrix_vec[i] <= vec[i])) return 0;
    }
    return 1;
}

int get_smaller_or_equal_processes(int * vec, int * matrix, int matrix_length, int vec_length) {
    int width = matrix_length/vec_length;
    int i, j;
    for(i = 0; i < width; i++) {
        int * test_vec = malloc(MAX_SIZE * sizeof(int));
        for(j = 0; j < vec_length; j++) {
            test_vec[j] = matrix[j + (i * vec_length)];
        }
        if (is_vec_smaller_or_equal(vec, test_vec, vec_length)) return i;
        free(test_vec);
    }
    return -1;
}

void print_all_unmarked_processes(int * vec, int length, int mark) {
    int i = 0;
    printf("[ ");
    for (i = 0; i < length; i++)
    {
        if(vec[i] != mark && i == length - 1) 
            printf(" %d", vec[i]);
        else if(vec[i] != mark)
            printf(" %d,", vec[i]);
        
    }
    printf(" ]\n");
}


void write_line_to_matrix(int * matrix, char * buffer, size_t buffer_length, FILE * fp) {
    int vec_index = 0;
    ssize_t buffer_line_length;
    while ((buffer_line_length = getline(&buffer, &buffer_length, fp)) != 1 && buffer_line_length != -1)
    {
        for (ssize_t i = 0; i < buffer_line_length; i++)
        {
            if (isdigit(buffer[i]))
            {
                matrix[vec_index] = buffer[i] - '0';
                vec_index++;
            }
        }
    }
}

// This algorithm is based on the supposition that the numbers at the data.txt file
// are written in the following encoding regarding the character defining the numbers below:
// p represents # of processes
// r represents # of resources
// e represents vector e
// a represents 4 vector a
// C represents matrix c
// R represents matrix r

int main(int argc, char const *argv[])
{
    char const * const filename = argv[1];
    if(argc < 2 || strlen(filename) < 3 || filename == NULL ) {
        perror("Invalid argument \n");
        exit(EXIT_FAILURE);
    } 

    printf("Reading the contents of %s \n", filename);

    FILE * fp;
    fp = fopen(filename, "r");
    if(fp == NULL) {
        printf("The file %s was not found \n", filename);
        perror("Invalid argument");
        exit(EXIT_FAILURE);
    }
    char * buffer = NULL;
    size_t buffer_length = 0;
    ssize_t line_length, buffer_line_length;
    int process_amount = 0, resource_amount = 0;
    char process_amount_id = 'p', resource_amount_id = 'r', vector_e_id = 'e', vector_a_id = 'a', matrix_c_id = 'C', matrix_r_id = 'R';

    int * vec_e = malloc(MAX_SIZE * sizeof(int));
    int * vec_a = malloc(MAX_SIZE * sizeof(int));
    int * matrix_c = malloc(MAX_SIZE * sizeof(int));
    int * matrix_r = malloc(MAX_SIZE * sizeof(int));
    int * new_vector = malloc(MAX_SIZE * sizeof(int));
    int * indexes = malloc(MAX_SIZE * sizeof(int));

    while ((line_length = getline(&buffer, &buffer_length, fp)) != -1)
    {
        if(line_length > 1) {
            if(buffer[0] == process_amount_id) {
                getline(&buffer, &buffer_length, fp);
                process_amount = buffer[0] - '0';
            } else if (buffer[0] == resource_amount_id) {
                getline(&buffer, &buffer_length, fp);
                resource_amount = buffer[0] - '0';
            } else if(buffer[0] == vector_e_id) {
                buffer_line_length = getline(&buffer, &buffer_length, fp);
                write_line_to_vector(vec_e, buffer, buffer_line_length);
            } else if(buffer[0] == vector_a_id) {
                buffer_line_length = getline(&buffer, &buffer_length, fp);
                write_line_to_vector(vec_a, buffer, buffer_line_length);
            } else if(buffer[0] == matrix_c_id) {
                write_line_to_matrix(matrix_c, buffer, buffer_length, fp);
            } else if(buffer[0] == matrix_r_id) {
                write_line_to_matrix(matrix_r, buffer, buffer_length, fp);
            }
        }
    }
    printf("The input data was: \n");
    printf("\nProcess amount = %d\n", process_amount);
    printf("Ressource amount = %d\n", resource_amount);
    printf("Vector e ");
    print_array(vec_e, resource_amount);
    printf("Vector a ");
    print_array(vec_a, resource_amount);
    printf("Matrix C ");
    print_array(matrix_c, process_amount * resource_amount);
    printf("Matrix R ");
    print_array(matrix_r, process_amount * resource_amount);
    printf("\n");

    int next_index;
    for(int i = 0; i < process_amount; i++) indexes[i] = i;
    while((next_index = get_smaller_or_equal_processes(vec_a, matrix_r, resource_amount * process_amount, resource_amount)) != -1) {
        printf("The reviewed process index is %d and the vector a is \n", next_index);
        print_array(vec_a, resource_amount);
        indexes[next_index] = INFINITY;
        for(int i = 0; i < resource_amount; i++) {
            vec_a[i] += matrix_c[i + (resource_amount * next_index)];
            matrix_r[i + (resource_amount * next_index)] = INFINITY;
        }
        if(vec_a[0] == INFINITY) break;
    }

    if(!vec_every(indexes, process_amount, INFINITY)) {
        printf("A deadlock was found, the involved processes are: ");
        print_all_unmarked_processes(indexes, process_amount, INFINITY);
    } else {
        printf("No deadlock was found :) \n");
    }
    free(vec_e);
    free(vec_a);
    free(matrix_c);
    free(matrix_r);
    free(new_vector);
    free(indexes);
    fclose(fp);
    return 0;
}
