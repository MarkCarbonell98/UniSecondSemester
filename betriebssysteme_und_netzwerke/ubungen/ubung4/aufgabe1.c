#include <stdio.h>
#include <pthread.h>
#define MAX 100

pthread_mutex_t mutex;
pthread_cond_t consumer_c, producer_c;

int buffer = 0;

void * producer(void * ptr) {
    int i;
    for(i = 1; i <= MAX; i++) {
        pthread_mutex_lock(&mutex);
        while(buffer != 0) pthread_cond_wait(&producer_c, &mutex);
        buffer = i;
        pthread_cond_signal(&consumer_c);
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit(0);
}

void * consumer(void * ptr) {
    int i;
    for ( i = 0; i < MAX; i++)
    {
        pthread_mutex_lock(&mutex);
        while(buffer == 0) pthread_cond_wait(&consumer_c, &mutex);
        buffer = 0;
        pthread_cond_signal(&producer_c);
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit(0);
}

int main(int argc, char const *argv[])
{
    pthread_t pro, con;
    pthread_mutex_init(&mutex, 0);
    pthread_cond_init(&consumer_c, 0);
    pthread_cond_init(&producer_c, 0);
    pthread_create(&con, 0, consumer, 0);
    pthread_create(&pro, 0, producer, 0);
    pthread_join(pro, 0);
    pthread_join(con, 0);
    pthread_cond_destroy(&consumer_c);
    pthread_cond_destroy(&producer_c);
    pthread_mutex_destroy(&mutex);

    return 0;
}





