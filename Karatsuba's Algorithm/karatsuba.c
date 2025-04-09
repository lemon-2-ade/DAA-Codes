#include "stdio.h"
#include "stdlib.h"
#include "math.h"

double fastMultiply (double a, double b) {
    if (a < 10 || b < 10) {
        return a * b;
    }

    int n = fmax(log10(a) + 1, log10(b) + 1);
    int mid = n / 2;
    double aL, aR, bL, bR, x1, x2, x3;

    aL = floor(a / pow(10, mid));
    aR = fmod(a, pow(10, mid));
    bL = floor(b / pow(10, mid));
    bR = fmod(b, pow(10, mid));

    x1 = fastMultiply(aL, bL);
    x2 = fastMultiply(aR, bR);
    x3 = fastMultiply(aL + aR, bL + bR);

    return (x1 * pow(10, 2 * mid)) + ((x3 - x2 - x1) * pow(10, mid)) + x2;
}

int main (void) {
    double num1, num2;

    printf("Enter the 1st no.: "); scanf("%lf", &num1);
    printf("Enter the 2nd no.: "); scanf("%lf", &num2);

    double result = fastMultiply(num1, num2);
    printf("Product: %lf", result);
}