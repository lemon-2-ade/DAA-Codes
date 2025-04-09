#include "stdio.h"

void Merge (int arr[], int low, int mid, int high) {

    int leftLength = mid - low + 1;
    int rightLength = high - mid;

    int left[leftLength], right[rightLength];
    
    for (int i = 0; i < leftLength; i++) {
        left[i] = arr[low+i];
    }
    for (int i = 0; i < rightLength; i++) {
        right[i] = arr[mid+1+i];
    }

    int i = 0, j = 0, k = low;
    while (i < leftLength && j < rightLength) {
        if (left[i] >= right[j]) {
            arr[k] = left[i++];
        } else {
            arr[k] = right[j++];
        } k++;
    }

    while (i < leftLength) {
        arr[k++] = left[i++];
    }
    while (j < rightLength) {
        arr[k++] = right[j++];
    }
}

void MergeSort (int arr[], int low, int high) {

    if (low < high) {
        int mid = (low + high) / 2;

        MergeSort(arr, low, mid);
        MergeSort(arr, mid + 1, high);
        Merge(arr, low, mid, high);
    }
}

/*int main (void) {
    
    int arr[] = { 34, -56, 29, 10, -23, -38, 100 };
    int length = sizeof(arr) / sizeof(int);

    MergeSort(arr, 0, length - 1);

    printf("Sorted array: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}*/