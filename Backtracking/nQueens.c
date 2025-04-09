#include "stdio.h"
#include "stdlib.h"
#include "stdbool.h"

int n;
int* col;

void printBoard() {
    char** board = (char**) malloc(n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        board[i] = (char*) malloc((n + 1) * sizeof(char));
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (col[i] == j) {
                board[i][j] = 'Q';
            } else {
                board[i][j] = '.';
            }
        } board[i][n] = '\0';
        printf("%s\n", board[i]);
    }
}

bool promising (int i) {
    for (int k = 0; k < i; k++) {
        if ((col[i] == col[k]) || (abs(col[i] - col[k]) == i - k)) {
            return false;
        } 
    } return true;
}

void solveNQueens(int i) {
    if (i == n) {
        printBoard();
        printf("\n");
    } else {
        for (int j = 0; j < n; j++) {
            col[i] = j;

            if (promising(i))
                solveNQueens(i + 1);
        }
    }
}

int main (void) {
    printf("Enter the value for n: ");
    scanf("%d", &n);

    col = (int*) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        col[i] = -1;
    }

    solveNQueens(0);
}