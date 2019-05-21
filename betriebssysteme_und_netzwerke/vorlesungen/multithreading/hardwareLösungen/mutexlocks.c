//mutex sind sperr locks
#include <thread_db.h>
#include <pthread.h>

typedef pthread_mutex_t mutex {

} mutex ;


init (mutex, attr); //erzeugt ein Mutex
destroy(mutex); //zertort mutex
lock(mutex); //blockiere oder erlange die Sperre
trylock(mutex); //erlange eine sperre oder fehler busy
unlock(mutex); //gebe sperre frei

pthread_cond_init(condition, attr);
pthread_cond_destroy(condition);
pthread_cond_wait(cond, mut);
pthread_cond_signal(condition);
pthread_cond_broadcast(condition);

//condition is the var, mut ein Mutex


//how