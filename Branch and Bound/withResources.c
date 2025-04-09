/* job selection! */

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int profit, deadline, resources;
} Job;

int compare (const void *a, const void *b) {
    return ((Job*)b)->profit - ((Job*)a)->profit; 
}

void branchAndBound (int index, Job jobs[], int nJobs, int* slots,
    int currentProfit, int* maxProfit, int currentResources, int maxResources) {
    
    if (index == nJobs) {
        if (currentProfit > *maxProfit && currentResources <= maxResources) {
            *maxProfit = currentProfit;
        } return;
    }

    for (int slot = jobs[index].deadline; slot > 0; slot--) {

        if (slots[slot] == 0) {
            slots[slot] = 1;
            
            branchAndBound(index + 1, jobs, nJobs, slots,
                currentProfit + jobs[index].profit, maxProfit,
                currentResources + jobs[index].resources, maxResources);
                
            slots[slot] = 0;
        }
    }

    branchAndBound(index + 1, jobs, nJobs, slots,
        currentProfit, maxProfit, currentResources, maxResources);
}

int getMaxProfit (Job jobs[], int nJobs, int maxResources) {

    // sorting in descending order accroding to the profit
    qsort(jobs, nJobs, sizeof(Job), compare);

    int maxDeadline = 0;
    for (int i = 0; i < nJobs; i++) {
        if (jobs[i].deadline > maxDeadline)
            maxDeadline = jobs[i].deadline;
    }   // obtaining the max deadline for making avilable slots

    int* slots = (int*) calloc(maxDeadline + 1, sizeof(int));
    int maxProfit = 0;

    branchAndBound(0, jobs, nJobs, slots, 0, &maxProfit, 0, maxResources);

    free(slots);
    return maxProfit;
} 

int main (void) {

    int maxResources = 5;
    int nJobs = 3;
    Job jobs[3] = {
        { 150, 3, 2 },
        { 100, 1, 3 },
        { 200, 2, 3 }
    };

    int maxProfit = getMaxProfit(jobs, nJobs, maxResources);
    printf("Maximum profit: %d", maxProfit);
}