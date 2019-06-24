#include "stdio.h"
#include "stdlib.h"

#define MAX_SIZE 100
#define INFINITY 2147483647

// Program sollte die prozesscheduling algorithmen simulieren. 
// Parameter: Quantum fur unterbrechbare algorithmen
// Input eine folge von laufzeiten, in reihenfolge des treffers
// Alle proz. starten in Wartezustand
// Scheduler kennt der Joblange

//output: tupelfolge (pi, ti), dh, welchen prozess wie lange lauft, in die korrekte reihenfolge
// Aufnumierte turn-around-zeit
// Strategien: FCFS (first come first served), SJF (shortest job first), SRTF(shortest remaining time first) und Round Robin 
// Startquantom q = 5.

// prozesse laufzeiten: 
// 5, 3, 12, 100, 1, 2, 3, 4, 5
// 5, 4, 3, 2, 1, 100, 12, 3, 5
// 23, 17, 31, 29, 71, 2, 5, 113

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

int * copy_int_array(int * arr, int length) {
    int * copy = malloc(sizeof(int) * length);
    for(int i = 0; i < length; i++) {
        copy[i] = arr[i];
    }
    return copy;
}

int find_minimum_index_array(int * arr, int length) {
    int temp, index;
    temp = arr[0]; index = 0;
    for(int i = 1; i < length; i++) {
        if(arr[i] < temp && arr[i] != 0) {
            temp = arr[i];
            index = i;
        }
    }
    return index;
}

int find_index_shortest_job_to_complete(int * arr, int length) {
    int * copy3 = malloc(sizeof(int) * length);
    int remaining_time = 0, result;
    for(int i = 0; i < length; i++) {
        if(i > 0 && arr[i] != INFINITY) {
            remaining_time += arr[i-1];
        }
        copy3[i] = remaining_time + arr[i];
    }
    result = find_minimum_index_array(arr, length);
    free(copy3);
    return result;
}

// int find_index_shortest_job_to_complete(int * arr, int length) {
//     int * copy3 = malloc(sizeof(int) * length);
//     int remaining_time = 0, result = find_minimum_index_array(copy3, length);
//     for(int i = 0; i < length; i++) {
//         if
//     }
//     result = find_minimum_index_array(copy3, length);
//     free(copy3);
//     return result;
// }



int main(int argc, char const *argv[])
{
    if(argc != 2 || argv[1] == NULL) {
        perror("Invalid argument!");
        exit(EXIT_FAILURE);
    }

    int quantum = atoi(argv[1]);
    printf("quantum: %d \n", quantum);

    const int process_amount = 9;
    const int process_array_amount = 3;
    int first_process_times[9] = {5,3,12,100,1,2,3,4,5};
    int second_process_times[9] = {5,4,3,2,1,100,12,3,5};
    int third_process_times[9] = {23, 17, 31, 29, 71, 2, 5, 113};

    int all_processes[3][9] = { {5, 3, 12, 100, 1, 2, 3, 4, 5},
                            {5, 4, 3, 2, 1, 100, 12, 3, 5},
                            {23, 17, 31, 29, 71, 2, 5, 113} };


    int turn_around_time = 0, old_time;
    int min_index = 0, element_with_shortest_time = 0, last_element = 0;

    printf("The first process execution times are: \n");
    print_array(first_process_times, process_amount);
    printf("The second process execution times are: \n");
    print_array(second_process_times, process_amount);
    printf("The third process execution times are: \n");
    print_array(third_process_times, process_amount - 1);
    printf("Starting First Come, First Served algorithm: \n");

    for(int i = 0; i < process_array_amount; i++) {
        turn_around_time = 0, old_time = 0;
        for(int j = 0; j < process_amount; j++) {
            if(all_processes[i][j] != 0) {
                if(j > 0) {
                    old_time += all_processes[i][j-1];
                    turn_around_time += old_time;
                }
                printf("(order: %d, time: %d)\n", j, all_processes[i][j]);
                if((j == process_amount-1)) printf("Total turn around time equals: %d \n\n", turn_around_time/process_amount);
                if(i == process_array_amount -1 && j == process_amount-2) printf("Total turn around time equals: %d \n\n", turn_around_time/(process_amount -1));
            }
        }
    }

    printf("Starting Shortest Job First algorithm: \n");
    min_index = 0, element_with_shortest_time = 0, last_element = 0;
    for(int i = 0; i < process_array_amount; i++) {
        turn_around_time = 0, old_time = 0;
        int * array_copy = copy_int_array(all_processes[i], process_amount);
        for(int j = 0; j < process_amount; j++) {
            if(all_processes[i][j] != 0) {
                min_index = find_minimum_index_array(array_copy, process_amount);
                element_with_shortest_time = array_copy[min_index];
                if(j>0) {
                    old_time += last_element;
                    turn_around_time += old_time;
                }
                last_element = element_with_shortest_time;
                printf("(order: %d, time: %d)\n", min_index, element_with_shortest_time);
                array_copy[min_index] = INFINITY;
                if((j == process_amount-1)) printf("Total turn around time equals: %d \n\n", turn_around_time/process_amount);
                if(i == process_array_amount -1 && j == process_amount-2) 
                    printf("Total turn around time equals: %d \n\n", turn_around_time/(process_amount -1));
            }
        }
        free(array_copy);
    }

    printf("Starting Shortest Remaining Time First algorithm: \n");
    min_index = 0; element_with_shortest_time = 0; last_element = 0;
    for (int i = 0; i < process_array_amount; i++)
    {
        turn_around_time = 0, old_time = 0;
        int *array_copy = copy_int_array(all_processes[i], process_amount);
        for (int j = 0; j < process_amount; j++)
        {
            if (all_processes[i][j] != 0)
            {
                min_index = find_index_shortest_job_to_complete(array_copy, process_amount);
                element_with_shortest_time = array_copy[min_index];
                if (j > 0)
                {
                    old_time += last_element;
                    turn_around_time += old_time;
                }
                last_element = element_with_shortest_time;
                printf("(order: %d, time: %d)\n", min_index, element_with_shortest_time);
                array_copy[min_index] = INFINITY;
                if ((j == process_amount - 1))
                    printf("Total turn around time equals: %d \n\n", turn_around_time / process_amount);
                if (i == process_array_amount - 1 && j == process_amount - 2)
                    printf("Total turn around time equals: %d \n\n", turn_around_time / (process_amount - 1));
            }
        }
        free(array_copy);
    }

    // int test[4] = {3,6,7,8};
    // int counter = 0, oldCounter = 0;
    // for (int i = 0; i < 4; i++)
    // {
    //     if(i > 0) {
    //         counter += test[i-1];
    //         oldCounter += counter;
    //     }
    //     printf("%d %d\n", counter, oldCounter);
    // }
    // find_index_shortest_job_to_complete(test, 4);
    return 0;
}
