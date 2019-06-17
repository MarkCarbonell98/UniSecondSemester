#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

void printArray(int * arr, int length) {
    int i = 0; 
    printf("[ ");
    for ( i = 0; i < length; i++)
    {
        if(i == length -1) printf("%d", arr[i]);
        else printf("%d,", arr[i]);
    }
    printf(" ]\n");
}

int main(int argc, char const *argv[])
{
    // int testArr[] = {};
    // int testArr1[] = {};
    // int testArr2[] = {};
    // int testArr3[] = {};
    // for(int i = 0; i < 100; i++) {testArr[i] = i; testArr1[i] = i; testArr2[i] = i; testArr3[i] = i;}
    // printArray(testArr, 100);
    // printArray(testArr1, 100);
    // printArray(testArr2, 100);
    // printArray(testArr3, 100);

    if(argc < 2 || strlen(argv[1]) < 3) {
        perror("Invalid argument \n");
        exit(EXIT_FAILURE);
    }

    int process_amount = 0, resource_amount = 0;
    int vector_e[MAX_SIZE], vector_a[MAX_SIZE], matrix_c[MAX_SIZE], matrix_r[MAX_SIZE];

    FILE * fp2;
    fp2 = fopen(argv[1], "r");
    char c;
    int line_count = 0, i = 0, j = 0, k = 0, l = 0;
    printf("The contents of %s are: \n", argv[1]);
    while((c = fgetc(fp2)) != EOF) {
        printf("%c",c);
        if(c == '\n') ++line_count;
        if(c != ' ' && c != '\n') {
            c = c == '0' ? c : c - '0';
            switch (line_count)
            {
                case 0:
                    process_amount = c;
                    break;
                case 1:
                    resource_amount = c;
                    break;
                case 2:
                    vector_e[i] = c;
                    i++;
                    break;
                case 3:
                    vector_a[j] = c;
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

    printArray(vector_e, resource_amount);
    printArray(vector_a, resource_amount);
    printArray(matrix_c, process_amount * resource_amount);
    printArray(matrix_r, process_amount * resource_amount);
    fclose(fp2);
    return 0;
}
