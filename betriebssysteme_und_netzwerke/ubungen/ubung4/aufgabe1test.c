#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
// #define NUM_THREADS 1
// #define NUM_THREADS 5
// #define NUM_THREADS 10
// #define NUM_THREADS 100

pthread_mutex_t mutex;
pthread_cond_t parent_cond, child_cond;

int childInnerCounter = 0, i = 0;


void * childThreadFunction(void * argument) {
    int tid;
    tid = *((int *) argument);
    ++i;
    while(1) {
        pthread_mutex_lock(&mutex);
        ++childInnerCounter;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main(int argc, char const *argv[])
{
    if(argc == 2) {
        pthread_mutex_init(&mutex, 0);
        char * input = argv[1];
        int n = atoi(input);
        pthread_t threads[n];
        int thread_args[n];
        int rc;
        int i;
        for(i = 0; i < n; ++i) {
            thread_args[i] = i;
            printf("In main: creating thread #%d \n", i);
            rc = pthread_create(&threads[i], NULL, childThreadFunction, (void *) &thread_args[i]);
            assert( 0 == rc);
        }

        wait(1);
        childInnerCounter = 0;
        sleep(3);

        printf("There were %d threads created, and the child thread counter is %d \n", i, childInnerCounter);

        pthread_mutex_destroy(&mutex);
        exit(EXIT_SUCCESS);
        return 0;
    } else {
        printf("You must insert the number of threads n to start the program, try again! \n");
        exit(EXIT_FAILURE);
        return 0;
    }
}
