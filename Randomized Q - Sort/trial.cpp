#include <algorithm>
#include <iostream>
#include <map>
#include <time.h>
#include <vector>

using namespace std;

int partition (vector<int> &arr, int low, int high) {
    int pivot = arr[low];
    int start = low, end = high;

    while (start < end) {
        while (arr[start] <= pivot && start < end) {
            start++;
        }
        while (arr[end] > pivot) {
            end--;
        }

        if (start < end) {
            swap(arr[start], arr[end]);
        }
    }

    swap(arr[low], arr[end]);
    return end;
}

int randomizedPartition (vector<int> &arr, int low, int high) {
    srand(time(NULL));

    int randomIndex = low + rand() % (high - low + 1);
    swap(arr[low], arr[randomIndex]);

    return partition(arr, low, high);
}

void randomizedQuicksort (vector<int> &arr, int low, int high) {
    if (low < high) {
        int position = randomizedPartition(arr, low, high);
        randomizedQuicksort(arr, low, position - 1);
        randomizedQuicksort(arr, position + 1, high);
    }
}

int main (void) {
    vector<int> arr = { 45, 67, -10, -39, 29, 10, -34, 74 };
    int length = arr.size();

    map<int, int> hashmap;
    for (int i = 0; i < length; i++) {
        hashmap[arr[i]] = i;
    }

    randomizedQuicksort(arr, 0, length - 1);
    for (int value: arr) {
        cout << value << ": " << hashmap[value] << endl;
    }
}