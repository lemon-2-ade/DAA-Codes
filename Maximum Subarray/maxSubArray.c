#include "stdio.h"
#include "stdlib.h"
#include "limits.h"

typedef struct {
    int low, high, sum;
} SubArray;

SubArray findMaxCrossSum (int* arr, int low, int mid, int high) {
    int leftSum = INT_MIN;
    int maxLeft = mid;
    int sum = 0;

    for (int i = mid; i >= low; i--) {
        sum += arr[i];
        if (sum > leftSum) {
            leftSum = sum;
            maxLeft = i;
        }
    }

    int rightSum = INT_MIN;
    int maxRight = mid + 1;
    sum = 0;

    for (int i = mid + 1; i <= high; i++) {
        sum += arr[i];
        if (sum > rightSum) {
            rightSum = sum;
            maxRight = i;
        }
    }

    SubArray value = { maxLeft, maxRight, leftSum + rightSum };
    return value;
}

SubArray findMaxSubarraySum (int* arr, int low, int high) {
    if (high == low) {
        SubArray value = { low, high, arr[low] };
        return value;
    }

    int mid = (low + high) / 2;

    SubArray left = findMaxSubarraySum(arr, low, mid);
    SubArray right = findMaxSubarraySum(arr, mid + 1, high);
    SubArray cross = findMaxCrossSum(arr, low, mid, high);

    if (left.sum >= right.sum && left.sum >= cross.sum) {
        return left;
    } else if (right.sum >= left.sum && right.sum >= cross.sum) {
        return right;
    } else {
        return cross;
    }
}

int main (void) {
    int arr[] = { 34, 56, 78, -10, 23, -67, 28 };
    int length = sizeof(arr) / sizeof(arr[0]);

    SubArray result = findMaxSubarraySum(arr, 0, length - 1);
    
    printf("Array: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }

    printf("\nMaximum sum: %d", result.sum);
    printf("\nIndices: (%d, %d)", result.low, result.high);
    
    return 0;
}