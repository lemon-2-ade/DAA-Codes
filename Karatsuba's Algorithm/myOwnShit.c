#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"

char* allocateMemory (int size) {
    char* string = (char*) malloc(size * sizeof(char));
    return string;
}

void freeMemory (char* variable) {
    if (variable)
        free(variable);
}

char* paddingStr (const char* str, int places) {
    int len = strlen(str) + places + 1;
    char* paddedStr = allocateMemory(len);

    memset(paddedStr, '0', places);
    strcpy(paddedStr + places, str);

    return paddedStr;
}

char* strValue (int number) {
    int digits = (int) log10(number) + 2;       // +2 for digit and null-terminator
    char* numStr = allocateMemory(digits);
    sprintf(numStr, "%d", number);

    return numStr;
}

char* addStrings(const char* num1, const char* num2) {
    int len1 = strlen(num1), len2 = strlen(num2);
    int maxLen = (len1 > len2)? len1 : len2;
    
    char* result = allocateMemory(maxLen + 1);      // +1 for potential carry;
    result[maxLen + 1] = '\0';

    int i = len1 - 1, j = len2 - 1, k = maxLen;
    int carry = 0;

    while (i >= 0 || j >= 0) {
        int sum = carry;
        if (i >= 0)
            sum += num1[i] - '0';
        
        if (j >= 0)
            sum += num2[j] - '0';

        result[k--] = (sum % 10) + '0';
        carry = sum / 10;
        i--; j--;
    }

    if (carry > 0) {
        result[k--] = carry + '0';
    } return result;
}

char* subtractStrings (const char* num1, const char* num2) {
    int len1 = strlen(num1), len2 = strlen(num2);
    int maxLen = len1;

    char* result = allocateMemory(maxLen);
    result[maxLen] = '\0';

    int i = len1 - 1, j = len2 - 1, k = maxLen - 1;
    int borrow = 0;

    while (i >= 0) {
        int difference = num1[i] - '0' - borrow;
        if (j >= 0)
            difference -= (num2[j] - '0');
        
        if (difference < 0) {
            difference += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }

        result[k--] = difference + '0';
        i--; j--;
    } return result;
}

char* powerOfTen (const char* number, int places) {
    char* zeroes = allocateMemory(places + 1);
    memset(zeroes, '0', places);
    zeroes[places] = '\0';
    
    int resultLen = strlen(number) + places + 1;
    char* result = allocateMemory(resultLen);
    strcpy(result, number); strcat(result, zeroes);

    return result;
}

char* fastMultiply (const char* a, const char* b) {
    int len1 = strlen(a), len2 = strlen(b);
    int n = 0, mid = 0;

    if (len1 < len2) {
        a = paddingStr(a, len2 - len1);
        n = len1;
    } else {
        b = paddingStr(b, len1 - len2);
        n = len2;
    } mid = n / 2;

    if (n == 1) {
        // int product = atoi(a) * atoi(b);
        int product = (a[0] - '\0') * (b[0] - '\0');
        return strValue(product);
    } else {
        char *aL = allocateMemory(mid + 1), *aR = allocateMemory(n - mid + 1);
        char *bL = allocateMemory(mid + 1), *bR = allocateMemory(n - mid + 1);

        strncpy(aL, a, mid); strncpy(aR, a + mid, n - mid);
        aL[mid] = aR[n - mid] = '\0';

        strncpy(bL, b, mid); strncpy(bR, b + mid, n - mid);
        bL[mid] = bR[n - mid] = '\0';

        char* x1 = fastMultiply(aL, bL);
        char* x2 = fastMultiply(aR, bR);
        char* x3 = fastMultiply(addStrings(aL, aR), addStrings(bL, bR));

        char* inter1 = powerOfTen(x1, n);
        char* inter2 = powerOfTen(subtractStrings(x3, addStrings(x1, x2)), mid);

        char* result =  addStrings(x1, addStrings(inter2, x2)); 

        freeMemory(aL);
        freeMemory(aR);
        freeMemory(bL);
        freeMemory(bR);
        freeMemory(x1);
        freeMemory(x2);
        freeMemory(x3);
        freeMemory(inter1);
        freeMemory(inter2); 

        return result;
    }
}

int main (void) {
    char* a = "124568689";
    char* b = "342348768";

    char* result = addStrings(a, b);
    // printf("%s", result);
    int summation = atoi("23") + atoi("35");
    printf("%d", summation);
}