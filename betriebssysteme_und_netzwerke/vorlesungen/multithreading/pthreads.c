#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define NUM_THREADS 5

void * TaskCode(void * argument) {
    int tid; 
    tid = *((int*) argument);
    printf("I am number %d\n", tid);
    return NULL;
}

int main(int argc, char const *argv[])
{
    pthread_t threads[NUM_THREADS];
    int thread_args[NUM_THREADS];
    int rc, i;
    for(i = 0; i < NUM_THREADS; i++) {
        thread_args[i] = i;
        printf("creating %d\n", i);
        rc = pthread_create(&threads[i], NULL, TaskCode, (void*) &thread_args[i]);
        assert(0 == rc);
    }
    //wait for the threads to complete
    for(i = 0; i < NUM_THREADS; i++) {
        rc = pthread_join(&threads[i], NULL);
        assert(0 == rc);
    }
    exit(0);


    return 0;
}
