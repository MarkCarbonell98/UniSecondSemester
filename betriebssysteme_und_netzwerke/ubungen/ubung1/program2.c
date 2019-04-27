// program 2
int main(int argc, char* argv[]) {
    int i = 0;
    if(fork() != 0) i += 2;
    if (fork() == 0) i -= 1;
    if(fork() != 0) i -= 1;
    if (fork() * i == 0) fork();
    return 0;
}