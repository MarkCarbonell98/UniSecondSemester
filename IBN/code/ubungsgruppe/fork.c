#include "stdio.h"
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

int main() {
	pid_t pid = fork();
	if(pid==0) {
		printf("I say bye before diying \n");
		char a[80];
		sprintf(a, "%i", pid);

		execl("/bin/echo", "echo", "this is the child", a , NULL);
		printf("I wont execute\n");
	} else {
		printf("I am the parent process\n");
		printf("the %i\n", pid);
		wait(0);
	}
}
