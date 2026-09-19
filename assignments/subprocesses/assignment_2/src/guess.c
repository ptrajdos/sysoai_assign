#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    srand((unsigned)time(NULL));

    int secret = rand() % 101;
    int guess;

    printf("READY\n");
    fflush(stdout);

    while (scanf("%d", &guess) == 1) {
        if (guess < secret) {
            printf("TOO_LOW\n");
        } else if (guess > secret) {
            printf("TOO_HIGH\n");
        } else {
            printf("CORRECT\n");
            fflush(stdout);
            break;
        }

        fflush(stdout);
    }

    return 0;
}