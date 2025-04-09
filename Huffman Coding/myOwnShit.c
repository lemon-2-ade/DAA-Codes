#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdbool.h"

#define MAX_TREE_HT 1000

struct HuffmanNode {
    char data;
    int frequency;
    struct HuffmanNode *left, *right;
};

struct HuffmanNode* createHuffmanNode (char data, int frequency) {
    struct HuffmanNode* root = (struct HuffmanNode*) malloc(sizeof(struct HuffmanNode));

    root->data = data;
    root->frequency = frequency;
    root->left = root->right = NULL;

    return root;
}

struct MinHeap {
    int size, capacity;
    struct HuffmanNode** array;
};

struct MinHeap* createMinHeap (int capacity) {
    struct MinHeap* minHeap = (struct MinHeap*) malloc(sizeof(struct MinHeap));

    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->array = (struct HuffmanNode**) malloc(capacity * sizeof(struct HuffmanNode*));

    return minHeap;
}

void swapNodes (struct HuffmanNode** a, struct HuffmanNode** b) {
    struct HuffmanNode* temp = *a;
    *a = *b;
    *b = temp;
}

void minHeapify (struct MinHeap* minHeap, int index) {
    int smallest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < minHeap->size && minHeap->array[left]->frequency < minHeap->array[smallest]->frequency)
        smallest = left;

    if (right < minHeap->size && minHeap->array[right]->frequency < minHeap->array[smallest]->frequency)
        smallest = right;

    if (smallest != index) {
        swapNodes(&minHeap->array[smallest], &minHeap->array[index]);
        minHeapify(minHeap, smallest);
    }
}

void buildMinHeap (struct MinHeap* minHeap) {
    int n = minHeap->size - 1;
    for (int i = (n - 1) / 2; i >= 0; i--)
        minHeapify(minHeap, i);
}

struct HuffmanNode* extractMin (struct MinHeap* minHeap) {
    struct HuffmanNode* minimum = minHeap->array[0];
    minHeap->array[0] = minHeap->array[minHeap->size - 1];

    --minHeap->size;
    minHeapify(minHeap, 0);

    return minimum;
}

void insertMinHeap (struct MinHeap* minHeap, struct HuffmanNode* node) {
    ++minHeap->size;
    int i = minHeap->size - 1;

    while (i && node->frequency < minHeap->array[(i - 1) / 2]->frequency) {
        minHeap->array[i] = minHeap->array[(i - 1) / 2];
        i = (i - 1) / 2;
    } minHeap->array[i] = node;
}

bool isSizeOne (struct MinHeap* minHeap) { return minHeap->size == 1; }
bool isLeaf (struct HuffmanNode* root) { return !(root->left) && !(root->right); }

struct HuffmanNode* buildHuffmanTree (char data[], int frequency[], int size) {
    struct MinHeap* minHeap = createMinHeap(size);

    for (int i = 0; i < size; i++) {
        minHeap->array[i] = createHuffmanNode(data[i], frequency[i]);
    } minHeap->size = size;

    buildMinHeap(minHeap);
    struct HuffmanNode *top, *left, *right;

    while (!isSizeOne(minHeap)) {
        left = extractMin(minHeap);
        right = extractMin(minHeap);

        top = createHuffmanNode('$', left->frequency + right->frequency);
        top->left = left; top->right = right;

        insertMinHeap(minHeap, top);
    }

    return extractMin(minHeap);
}

void printHuffmanCodes (struct HuffmanNode* root, char* currentCode, char** huffmanCodes) {
    if (root->left) {
        strcat(currentCode, "0");
        printHuffmanCodes(root->left, currentCode, huffmanCodes);
        currentCode[strlen(currentCode) - 1] = '\0';
    }

    if (root->right) {
        strcat(currentCode, "1");
        printHuffmanCodes(root->right, currentCode, huffmanCodes);
        currentCode[strlen(currentCode) - 1] = '\0';
    }

    if (isLeaf(root)) {
        printf("%c: %s\n", root->data, currentCode);
        huffmanCodes[(int) root->data] = strdup(currentCode);
    }
}

int main (void) {
    int numCharacters = 6;
    char data[] = {'f', 'b', 'c', 'e', 'g', 'a'};
    int frequency[] = {34, 56, 29, 10, 23, 40};

    struct HuffmanNode* root = buildHuffmanTree(data, frequency, numCharacters);

    char currentCode[1000] = { 0 };
    char* huffmanCodes[256] = { 0 };

    printHuffmanCodes(root, currentCode, huffmanCodes);
}