#include <stdio.h>
#include <string.h>

void run(char *st, int l) {
#include "day16vars.h"
    char tempa[20];
    char tempb[20];
    char t;
    tempa[16] = 0;
    tempb[16] = 0;
    short i = 0;

    while (i < l) {
        tempa[i] = st[maparray[i]];
        i++;
    }

    // Spin
    i = l - spin;
    short j = 0;
    while (i < l) {
        tempb[j++] = tempa[i++];
    }
    
    i = 0;
    while (i < (l - spin)) {
        tempb[j++] = tempa[i++];
    }

    // Map
    i = 0;
    while (i < l) {
        st[i] = translate[tempb[i] - 97];
        i++;
    }
}

int main() {
    char st[] = "abcdefghijklmnop";
    short len = strlen(st);

    run(st, len);
    printf("%s\n", st);
    int i = 0;
    while (++i < 1000000000) {
        run(st, len);
    }

    printf("%s\n", st);
}