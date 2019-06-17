#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

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

// This algorithm is based on the supposition that the numbers at the data.txt file
// are written in the following line order:
// line 1 # of processes
// line 2 # of resources
// line 3 vector e
// line 4 vector a
// line 5 matrix c
// line 6 matrix r

int main(int argc, char const *argv[])
{
    char const *const filename = argv[1];
    if (argc < 2 || strlen(filename) < 3 || filename == NULL)
    {
        perror("Invalid argument \n");
        exit(EXIT_FAILURE);
    }

    printf("Reading the contents of %s \n", filename);

    FILE *fp;
    fp = fopen(filename, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);
    char *buffer = NULL;
    size_t length = 0;
    ssize_t line_length;

    int process_amount = 0, resource_amount = 0;
    int *vec_e = malloc(MAX_SIZE * sizeof(int));
    int *vec_a = malloc(MAX_SIZE * sizeof(int));
    int *matrix_c = malloc(MAX_SIZE * sizeof(int));
    int *matrix_r = malloc(MAX_SIZE * sizeof(int));

    int line_count = 0, i = 0, j = 0, k = 0, l = 0;
    char c;
    printf("The contents of %s are: \n", argv[1]);
    while ((c = fgetc(fp)) != EOF)
    {
        printf("%c", c);
        if (c == '\n')
            ++line_count;
        if (c != ' ' && c != '\n')
        {
            c = c == '0' ? 0 : c - '0';
            switch (line_count)
            {
            case 0:
                process_amount = c;
                break;
            case 1:
                resource_amount = c;
                break;
            case 2:
                vec_e[i] = c;
                i++;
                break;
            case 3:
                vec_a[j] = c;
                j++;
                break;
            case 4:
                matrix_c[k] = c;
                k++;
                break;
            case 5:
                matrix_r[l] = c;
                l++;
                break;
            default:
                break;
            }
        }
    }

    printf("\nProcess amount = %d\n", process_amount);
    printf("Ressource amount = %d\n", resource_amount);
    printArray(vec_e, i);
    printArray(vec_a, j);
    printArray(matrix_c, k);
    printArray(matrix_r, l);
    free(vec_e);
    free(vec_a);
    free(matrix_c);
    free(matrix_r);

    fclose(fp);
    return 0;
}
