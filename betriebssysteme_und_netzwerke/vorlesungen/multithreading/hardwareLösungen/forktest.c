#include <stdio.h>
#include <sys/sysinfo.h>

fork();
fork();
fork();

sleep(10);

printf("hellou from prozess", getpid(), getppid());
