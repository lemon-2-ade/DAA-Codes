#include "stdio.h"
#include "stdlib.h"
#include "limits.h"
#include "mergeSort.c"

#define MAX 10

int minMaxTime = INT_MAX;

int getMax (int arr[], int size) {

    int maximum = arr[0];
    for (int i = 1; i < size; i++) {
        if (maximum < arr[i])
            maximum = arr[i];
    }

    return maximum;
}

void assignTasks (int jobTimes[], int nJobs, int workers[], int nWorkers, int jobIndex) {

    if (jobIndex == nJobs) {
        int maxTime = getMax(workers, nWorkers);

        if (maxTime < minMaxTime) {
            minMaxTime = maxTime;
        } return;
    }

    for (int i = 0; i < nWorkers; i++) {
        if (workers[i] + jobTimes[jobIndex] >= minMaxTime) {
            continue;
        }

        workers[i] += jobTimes[jobIndex];
        assignTasks(jobTimes, nJobs, workers, nWorkers, jobIndex + 1);
        workers[i] -= jobTimes[jobIndex];

        if (workers[i] == 0) {
            break;
        } 
    }
}

int main (void) {

    int nJobs, nWorkers;

    printf("Enter the number of jobs: ");
    scanf("%d", &nJobs);
    
    int jobTimes[nJobs];
    printf("Enter the time for each job: ");
    for (int i = 0; i < nJobs; i++) {
        scanf("%d", &jobTimes[i]);
    }

    printf("Enter the number of workers: ");
    scanf("%d", &nWorkers);

    // sorting jobTimes in descending order
    MergeSort(jobTimes, 0, nJobs - 1);

    int workers[MAX] = { 0 };
    assignTasks(jobTimes, nJobs, workers, nWorkers, 0);
    printf("Min-max time: %d", minMaxTime);

    return 0;
}