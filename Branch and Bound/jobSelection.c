#include "stdio.h"
#include "stdlib.h"
#include "limits.h"

typedef struct {
    int profit, deadline;
} Job;

#define MAX 1000

int compare (const void *a, const void *b) {
    return ((Job*)a)->profit - ((Job*)b)->profit;
}

void branchAndBound (int index, int nJobs, int usedSlots[], int currentProfit, int *maxProfit, Job jobs[]) {

    if (index == nJobs) {
        if (currentProfit > *maxProfit) {
            *maxProfit = currentProfit;
        } return;
    }

    for (int slot = jobs[index].deadline; slot > 0; slot--) {
        if (usedSlots[slot] == 0) {
            usedSlots[slot] = 1;
            branchAndBound(index + 1, nJobs, usedSlots, currentProfit + jobs[index].profit, maxProfit, jobs);
            usedSlots[slot] = 0;
        }
    }

    branchAndBound(index + 1, nJobs, usedSlots, currentProfit, maxProfit, jobs);
}

int getMaxProfit (Job jobs[], int nJobs) {

    qsort(jobs, nJobs, sizeof(Job), compare);

    int maxDeadline = 0;
    for (int i = 0; i < nJobs; i++) {
        if (jobs[i].deadline > maxDeadline)
            maxDeadline = jobs[i].deadline;
    }

    int usedSlots[MAX] = { 0 };
    int maxProfit = 0;

    branchAndBound(0, nJobs, usedSlots, 0, &maxProfit, jobs);

    return maxProfit;
}

int main (void) {

    int nJobs = 3;
    Job jobs[3] = {
        { 50, 2 },
        { 20, 1 },
        { 30, 2 }
    };

    int maxProfit = getMaxProfit(jobs, nJobs);
    printf("Maximum profit: %d", maxProfit);
    
    return 0;
}