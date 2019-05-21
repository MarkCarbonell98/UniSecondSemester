#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// FABIAN REGNERY, JUSTIN SOSTMANN, MARCOS CARBONELL
// TUTOR ERIK KOYNOV

// aufgabe a)
/*
    mit 1 thread 
    There were 1 threads created, and the mutex was passed 86800789 times

    mit 5 threads
    There were 5 threads created, and the mutex was passed 25145018 times

    mit 10 threads
    There were 10 threads created, and the mutex was passed 24597491 times

    mit 100 threads
    There were 100 threads created, and the mutex was passed 24267995 times

    Der anzahl ist nicht gleich auf alle threads verteilt. Je mehr threads erzeugt werden, desto weniger wird der Mutex zugeteilt.

*/

/* AUFGABE B 

    den tests werden auf den core #3 ausgeführt mit taskset -c 3 ./aufgabe1.exe <num-of-threads>

    mit 1 thread 
    There were 1 threads created, and the mutex was passed 86967742 times

    mit 5 threads
    There were 5 threads created, and the mutex was passed 86621738 times

    mit 10 threads
    There were 10 threads created, and the mutex was passed 86973668 times

    mit 100 threads
    There were 100 threads created, and the mutex was passed 86985212 times

    In dem Fall wird der Mutex in fast konstanter Weise an die Threads zugeteilt.
    Da das Program nur von einen Core ausgeführt wird, dann wird der Mutex nicht von andere Cores blockiert um erhöht zu werden, was natürlich Zeit verbraucht, und die Fairness erniedrigt. Jetzt können wir sagen dass die Fairness sich erhöht hat wegen die ausführung auf einen einzigen Core.

*/

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

        printf("There were %d threads created, and the mutex was passed %d times\n", i, childInnerCounter);

        pthread_mutex_destroy(&mutex);
        exit(EXIT_SUCCESS);
        return 0;
    } else {
        printf("You must insert the number of threads n to start the program, try again! \n");
        exit(EXIT_FAILURE);
        return 0;
    }
}


