#include  <stdlib.h>

int main() {
    if (fork() > 0) sleep(1000);
    else exit(0);
    return 0;
}
