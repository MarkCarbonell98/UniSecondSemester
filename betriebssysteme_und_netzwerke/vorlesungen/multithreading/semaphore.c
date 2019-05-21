typedef struct
{
    int count; 
    struct process * list;
} semaphore ;

wait(semaphore * S) {
    //disable_interrupts()
    S->count--;
    if(S->count < 0) {
        //add to S->list
        // enable_interrupts()
        block();
    }
}

signal(semaphore *S) {
    //disable_interrupts()
    S->count++;
    if(S->count <= 0) {
        // get and remove 
        wakeup(/*name of process*/);
    } else {
        //
    }
    // enable_interrupts()process p from list
}
