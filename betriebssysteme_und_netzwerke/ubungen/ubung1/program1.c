
//program 1
int main(int argc, char* argv[]) {
    int i = 0;
    if(fork() != 0) i++;
    if(i != 0) fork();
    if(fork() != 0 || i != 0) i++;
    if(fork() == 0 && i == 0) fork();
    return 0;
}

