#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

typedef struct {
    int product, start, end;
} SubArray;

long long max(long long a, long long b) {
    return (a > b) ? a : b;
}

long long min(long long a, long long b) {
    return (a < b) ? a : b;
}

int partition(int* arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            ++i;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

int randomizedPartition(int* arr, int low, int high) {
    srand(time(NULL));

    int randomIndex = low + rand() % (high - low + 1);
    int temp = arr[randomIndex];
    arr[randomIndex] = arr[high];
    arr[high] = temp;

    return partition(arr, low, high);
}

void randomizedQuicksort(int* arr, int low, int high) {
    if (low < high) {
        int pi = randomizedPartition(arr, low, high);
        randomizedQuicksort(arr, low, pi - 1);
        randomizedQuicksort(arr, pi + 1, high);
    }
}

SubArray getMaxProductSubarray(int* arr, int n) {
    SubArray result = {arr[0], 0, 0};

    if (n == 0) {
        result.product = 0;
        return result;
    }

    long long maxProduct = arr[0];
    long long minProduct = arr[0];
    int start = 0;
    int end = 0;
    int tempStart = 0;

    for (int i = 1; i < n; i++) {
        if (arr[i] == 0) {
            maxProduct = 0;
            minProduct = 0;
            tempStart = i + 1;
        } else {
            long long tempMax = maxProduct;
            maxProduct = max(max((long long)arr[i], maxProduct * arr[i]), minProduct * arr[i]);
            minProduct = min(min((long long)arr[i], tempMax * arr[i]), minProduct * arr[i]);

            if (maxProduct > result.product) {
                result.product = maxProduct;
                result.start = tempStart;
                result.end = i;
            }
        }
    }

    return result;
}

int main(void) {

    int n = 4;
    int arr[4] = { 1, 7, 4, 9 };

    int* sortedArr = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        sortedArr[i] = arr[i];
    }

    randomizedQuicksort(sortedArr, 0, n - 1);

    printf("Sorted Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", sortedArr[i]);
    }

    SubArray result = getMaxProductSubarray(sortedArr, n);
    printf("\nMaximum product: %d", result.product);

    printf("\nMaximum subarray: ");
    for (int i = result.start; i <= result.end; i++) {
        printf("%d ", sortedArr[i]);
    }

    free(sortedArr);

    return 0;
}