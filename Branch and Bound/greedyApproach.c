#include "stdio.h"
#include "stdlib.h"
#include "mergeSort.c"

typedef struct {
    int profit, deadline;
} Project;

int compare (const void *a, const void *b) {
    return ((Project*)b)->profit - ((Project*)a)->profit;
}

int findMaxProfit (Project projects[], int nJobs) {

    // sorting the projects in descending order by their profit
    qsort(projects, nJobs, sizeof(Project), compare);

    // obtaining the maximum deadline
    int maxDeadline = projects[0].deadline;
    for (int i = 1; i < nJobs; i++) {
        if (maxDeadline < projects[i].deadline)
            maxDeadline = projects[i].deadline;
    }

    int slots[maxDeadline+1];
    for (int i = 0; i <= maxDeadline; i++) {
        slots[i] = -1;
    }

    int maxProfit = 0;
    for (int i = 0; i < nJobs; i++) {
        int availableSlot = projects[i].deadline;

        while (availableSlot > 0 && slots[availableSlot] != -1)
            availableSlot--;
        
        if (availableSlot > 0) {
            slots[availableSlot] = i;
            maxProfit += projects[i].profit;
        }
    }

    return maxProfit;
}

int main (void) {

    int nJobs;
    printf("Enter the number of jobs: ");
    scanf("%d", &nJobs);

    Project projects[nJobs];
    for (int i = 0; i < nJobs; i++) {
        printf("Enter the profit and deadline: ");
        scanf("%d %d", &projects[i].profit, &projects[i].deadline);
    }

    int result = findMaxProfit(projects, nJobs);
    
    return 0;
}