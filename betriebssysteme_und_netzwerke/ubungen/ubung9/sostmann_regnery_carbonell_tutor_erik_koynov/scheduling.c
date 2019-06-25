#include "stdio.h"
#include "stdlib.h"

#define MAX_SIZE 100
#define INFINITY 2147483647

int every_element_equals(int *vec, int length, int item)
{
    for (int i = 0; i < length; i++)
    {
        if (vec[i] != item)
            return 0;
    }
    return 1;
}

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

int *copy_int_array(int *arr, int length)
{
    int *copy = malloc(sizeof(int) * length);
    for (int i = 0; i < length; i++)
    {
        copy[i] = arr[i];
    }
    return copy;
}

int find_minimum_index(int *arr, int length)
{
    int temp, index;
    temp = arr[0];
    index = 0;
    for (int i = 1; i < length; i++)
    {
        if (arr[i] < temp && arr[i] != 0)
        {
            temp = arr[i];
            index = i;
        }
    }
    return index;
}

int find_smallest_execution_time(int *arr, int length)
{
    int temp, index;
    temp = arr[0];
    index = 0;
    for (int i = 1; i < length; i++)
    {
        if (arr[i] < temp && arr[i] != 0)
        {
            temp = arr[i];
            index = i;
        }
    }
    return temp;
}

int find_shortest_remaining_time(int *arr, int length)
{
    int temp, index;
    temp = arr[0];
    index = 0;
    for (int i = 1; i < length; i++)
    {
        if (arr[i] < temp && arr[i] != 0)
        {
            temp = arr[i];
            index = i;
        }
    }

    // checks whether a new process has arrived with a shorter processing time, if there is one, then it returns the index
    for (int i = 0; i < length; i++)
    {
        if (arr[i] < temp && arr[i] != 0)
        {
            return i;
        }
    }
    return index;
}

int main(int argc, char const *argv[])
{
    if (argc != 2 || argv[1] == NULL)
    {
        perror("Invalid argument!");
        exit(EXIT_FAILURE);
    }

    int quantum = atoi(argv[1]);
    printf("quantum: %d \n", quantum);

    const int process_amount = 9;
    const int process_array_amount = 3;
    int first_process_times[9] = {5, 3, 12, 100, 1, 2, 3, 4, 5};
    int second_process_times[9] = {5, 4, 3, 2, 1, 100, 12, 3, 5};
    int third_process_times[9] = {23, 17, 31, 29, 71, 2, 5, 113};

    int all_processes[3][9] = {{5, 3, 12, 100, 1, 2, 3, 4, 5},
                               {5, 4, 3, 2, 1, 100, 12, 3, 5},
                               {23, 17, 31, 29, 71, 2, 5, 113}};

    int turn_around_time = 0, old_time;
    int min_index = 0, element_with_shortest_time = 0, last_element = 0;

    printf("The first process execution times are: \n");
    print_array(first_process_times, process_amount);
    printf("The second process execution times are: \n");
    print_array(second_process_times, process_amount);
    printf("The third process execution times are: \n");
    print_array(third_process_times, process_amount - 1);

    printf("Starting First Come, First Served algorithm: \n");
    for (int i = 0; i < process_array_amount; i++)
    {
        turn_around_time = 0, old_time = 0;
        for (int j = 0; j < process_amount; j++)
        {
            if (all_processes[i][j] != 0)
            {
                if (j > 0)
                {
                    old_time += all_processes[i][j - 1];
                    turn_around_time += old_time;
                }
                printf("(order: %d, time: %d)\n", j, all_processes[i][j]);
                if ((j == process_amount - 1))
                    printf("Total turn around time equals: %d \n\n", turn_around_time / process_amount);
                if (i == process_array_amount - 1 && j == process_amount - 2)
                    printf("Total turn around time equals: %d \n\n", turn_around_time / (process_amount - 1));
            }
        }
    }

    printf("Starting Shortest Job First algorithm: \n");
    min_index = 0, element_with_shortest_time = 0, last_element = 0;
    for (int i = 0; i < process_array_amount; i++)
    {
        turn_around_time = 0, old_time = 0;
        int *array_copy = copy_int_array(all_processes[i], process_amount);
        for (int j = 0; j < process_amount; j++)
        {
            if (all_processes[i][j] != 0)
            {
                min_index = find_minimum_index(array_copy, process_amount);
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

    // In the exercise sheet is not clearly specified how we should demonstrate that the algorithm simulates
    // the appereance of shorter jobs during execution, because the jobs are already fixed. I programmed the functionality to stop processes in the case a new one "arrives" during execution.
    printf("Starting Shortest Remaining Time First algorithm: \n");
    min_index = 0;
    element_with_shortest_time = 0;
    last_element = 0;
    for (int i = 0; i < process_array_amount; i++)
    {
        turn_around_time = 0, old_time = 0;
        int *array_copy = copy_int_array(all_processes[i], process_amount);
        for (int j = 0; j < process_amount; j++)
        {
            if (all_processes[i][j] != 0)
            {
                min_index = find_shortest_remaining_time(array_copy, process_amount);
                element_with_shortest_time = array_copy[min_index];
                int smallest_value;
                //comparing tb with tr
                if ((smallest_value = find_smallest_execution_time(array_copy, process_amount)) < array_copy[min_index])
                {
                    // interrupting actual process and moving to the next one
                    continue;
                }
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

    printf("Starting Round Robin algorithm: \n");
    for (int i = 0; i < process_array_amount; i++)
    {
        turn_around_time = 0, old_time = 0;
        int *array_copy = copy_int_array(all_processes[i], process_amount);
        for (int j = 0;; j++)
        {
            if (all_processes[i][j] != 0)
            {
                if (i == process_array_amount - 1 && j == process_amount - 2 && every_element_equals(array_copy, process_amount, 0))
                {
                    printf("Total turn around time equals: %d \n\n", turn_around_time / (process_amount - 1));
                    break;
                }

                if (every_element_equals(array_copy, process_amount, 0))
                {
                    printf("Total turn around time equals: %d \n\n", turn_around_time / process_amount);
                    break;
                }
                if (j >= process_amount)
                    j = 0; //turning the array into a circular list
                if (array_copy[j] > 0)
                {
                    if (array_copy[j] > quantum)
                    {
                        printf("(order: %d, time: %d)\n", j, array_copy[j]);
                        array_copy[j] -= quantum;
                        if (j > 0)
                        {
                            old_time += quantum;
                        }
                    }
                    else
                    {
                        printf("(order: %d, time: %d)\n", j, array_copy[j]);
                        array_copy[j] = 0;
                        if (j > 0 && array_copy[j - 1] > 0)
                        {
                            old_time += array_copy[j - 1];
                            turn_around_time += old_time;
                        }
                    }
                }
            }
        }
        free(array_copy);
    }
    return 0;
}
