#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef struct {
    char* lcs;
    int lcsLength;
} LCS;

int getMax(int x, int y) {
    return (x > y) ? x : y;
}

LCS getLCS (char* x, int m, char* y, int n) {
    LCS result;

    int** dp = (int**) malloc((m + 1) * sizeof(int*));
    for (int i = 0; i < m + 1; i++) {
        dp[i] = (int*) calloc((n + 1), sizeof(int));
    }

    for (int i = 1; i < m + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            if (x[i-1] == y[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = getMax(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    int index = dp[m][n];
    result.lcsLength = index;

    char* lcs = (char*) malloc((index + 1) * sizeof(char));
    lcs[index] = '\0';

    int i = m, j = n;
    while (i > 0 && j > 0) {
        if (x[i-1] == y[j-1]) {
            lcs[index-1] = x[i-1];
            i--; j--;
            index--;
        } else if (dp[i-1][j] > dp[i][j-1]) {
            i--;
        } else {
            j--;
        }
    } result.lcs = lcs;

    return result;
}

char* getInputString (int length) {
    char* inputString = (char*) malloc((length + 1) * sizeof(char));
    char letter;
    int count = 0;

    while ((letter = getchar()) != '\n') {
        inputString[count++] = letter;
    } inputString[count] = '\0';

    return inputString;
}

int main (void) {
    int m, n;
    
    printf("Enter no. of chars. for 1st word: "); scanf("%d", &m);
    printf("Enter no. of chars. for 2nd word: "); scanf("%d", &n);
    
    getchar();
    
    printf("Enter the 1st word: ");
    char* x = getInputString(m);
    printf("Enter the 1dn word: ");
    char* y = getInputString(n);

    LCS result = getLCS(x, m, y, n);

    printf("LCS: %s\n", result.lcs);
    printf("Length of LCS: %d", result.lcsLength);
}