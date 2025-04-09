/* matrix chain multiplication! */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int minScalarProduct;
    int **s;
} MatrixChain;

MatrixChain maxtrixChain (int p[], int size) {

    int n = size - 1;
    int** m = (int*) malloc(n * sizeof(int*));
    int** s = (int*) malloc(n * sizeof(int*));

    for (int i = 0; i < n; i++) {
        m[i] = (int*) calloc(n, sizeof(int));
        s[i] = (int*) calloc(m, sizeof(int));    
    }

    for (int l = 1; l < n; l++) {
        for (int i = 0; i < n - l; i++) {
            int j = i + l;
            m[i][j] = INT_MAX;

            for (int k = i; k < j; k++) {
                int q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1];

                if (q < m[i][j]) {
                    m[i][j] = q;
                    s[i][j] = k;
                }
            }
        }
    }

    MatrixChain result = { m[0][n-1], s };
    return result;
}

void printOptimalParenthesis (int** s, int i, int j) {

    if (i == j) {
        printf("A%d", i + 1);
    } else {
        printf("(");
        printOptimalParenthesis(s, i, s[i][j]);
        printOptimalParenthesis(s, s[i][j] + 1, j);
        printf(")");
    }
}

int main (void) {

    int matrices[] = { 4, 10, 3, 12, 20, 7 };
    int size = sizeof(matrices) / sizeof(int);

    MatrixChain result = maxtrixChain(matrices, size);
    printf("Minimum scalar multiplications: %d\n", result.minScalarProduct);

    printf("Optimal parenthesization: ");
    printOptimalParenthesis(result.s, 0, size - 2);

    return 0;
}