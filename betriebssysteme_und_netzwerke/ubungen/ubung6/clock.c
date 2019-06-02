#include <stdio.h>
#include <stdlib.h>

int arrayIncludes(int * array, int length, int includes) {
    int i;
    for(i = 0; i < length; i++){
        if(array[i] == includes) return 1;
    }
    return 0;
}

void printArray(int * array, int length) {
    printf("\n[\n");
    int i;
    for(i = 0; i < length; i++){
        printf(" %d, \n", array[i]);
    }
    printf("] \n");
}

int main(int argc, char const *argv[])
{
    int anzahl_seitenrahmen = atoi(argv[1]);
    int speicher[anzahl_seitenrahmen];
    int clock_ptr = 0;
    int folgeA[] = {7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1};
    int folgeB[] = {2,3,2,1,5,2,4,5,3,2,5,2};

    long int folgeALength = sizeof(folgeA)/sizeof(folgeA[0]);
    long int folgeBLength = sizeof(folgeB)/sizeof(folgeB[0]);
    int i = 0, speicherIndex = 0; 
    printf("Einfache Clock Algorithmus A");
    for(i = 0; i < folgeALength; i++) {
        if(!arrayIncludes(speicher, folgeALength, folgeA[i]) || i < anzahl_seitenrahmen) {
            speicher[speicherIndex] = folgeA[i];
            ++speicherIndex;
            if(speicherIndex == anzahl_seitenrahmen) speicherIndex = 0;
            printArray(speicher, anzahl_seitenrahmen);
        } else {
            speicher[clock_ptr] = folgeA[i];
            clock_ptr++;
            if(clock_ptr == anzahl_seitenrahmen) clock_ptr = 0;
            printArray(speicher, anzahl_seitenrahmen);
        }
    }

    printf("Einfache Clock Algorithmus B"); 
    i = 0, speicherIndex = 0;
    for(i = 0; i < folgeBLength; i++) {
        if(!arrayIncludes(speicher, folgeBLength, folgeA[i]) || i < anzahl_seitenrahmen) {
            speicher[speicherIndex] = folgeB[i];
            ++speicherIndex;
            if(speicherIndex == anzahl_seitenrahmen) speicherIndex = 0;
            printArray(speicher, anzahl_seitenrahmen);
        } else {
            speicher[clock_ptr] = folgeB[i];
            clock_ptr++;
            if(clock_ptr == anzahl_seitenrahmen) clock_ptr = 0;
            printArray(speicher, anzahl_seitenrahmen);
        }
    }
    return 0;
}
