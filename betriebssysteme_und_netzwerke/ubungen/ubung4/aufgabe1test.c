#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define NUM_THREADS 100

pthread_mutex_t mutex;
pthread_cond_t parent_thread_cond, child_thread_cond;

int counter = 0;

void * thread_report(void * argument) {
    int tid;
    tid = *((int *) argument);
    printf("I am the number %d, and i = %d \n", tid, counter);
    while(1) {
        pthread_mutex_lock(&mutex);
        ++counter;
        pthread_cond_signal(&parent_thread_cond);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main(int argc, char const *argv[])
{

    if(argc == 1) {
        printf("You must enter the amount of threads n, try again \n");
        exit(EXIT_SUCCESS);
    }

    printf("n = %s \n", argv[1]);
    int n = (int)(*argv[1]);
    printf("n = %s \n", argv[1]);

    if(argc == 2) {
        pthread_t threads[n];
        int thread_args[n];
        int rc;
        int i;
        for(i = 0; i < n; ++i) {
            thread_args[i] = i;
            printf("In main: creating thread #%d \n", i);
            rc = pthread_create(&threads[i], NULL, thread_report, (void *) &thread_args[i]);
            assert( 0 == rc);
        }
        wait(NULL);
        counter = 0;
        fflush(stdout);
        sleep(3);

        printf("the counter state is: %d \n", counter);

    }
    exit(EXIT_SUCCESS);
    return 0;
}
