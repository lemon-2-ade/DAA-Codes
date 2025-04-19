#include <iostream>
#include <limits>

using namespace std;
int V;

void displayAjacencyMatrix (int** graph) {
    cout << "Adjacency matrix:-" << endl;
    for (int u = 0; u < V; u++) {
        for (int v = 0; v < V; v++) {
            cout << graph[u][v] << " ";
        } cout << endl;
    }
}

bool dfs (int** residualGraph, int source, int sink, int* parent) {
    bool visited[V] = { false };
    int stack[V], top = -1;

    visited[source] = true;
    stack[++top] = source;
    parent[source] = -1;

    while (top != -1) {
        int u = stack[--top];

        for (int v = 0; v < V; v++) {
            if (!visited[v] && residualGraph[u][v] > 0) {
                parent[v] = u;

                if (v == sink)
                    return true;
                
                stack[++top] = v;
                visited[v] = true;
            }
        }
    } return false;
}

int findMaxFlow (int** graph, int source, int sink) {
    int** residualGraph = (int**) malloc(V * sizeof(int*));
    for (int u = 0; u < V; u++) {
        residualGraph[u] = (int*) calloc(V, sizeof(int));

        for (int v = 0; v < V; v++)
            residualGraph[u][v] = graph[u][v];
    }

    int maxFlow = 0;
    int* parent = (int*) malloc(V * sizeof(int));

    while (dfs(residualGraph, source, sink, parent)) {
        int pathFlow = INT_MAX;

        int v = sink;
        while (v != source) {
            int u = parent[v];
            pathFlow = (residualGraph[u][v] < pathFlow) ? residualGraph[u][v] : pathFlow;
            int v = parent[v];
        }   // for obtaining the bottleneck value

        v = sink;
        while (v != source) {
            int u = parent[v];
            residualGraph[u][v] -= pathFlow;
            residualGraph[v][u] += pathFlow;
            int v = parent[v];
        } maxFlow += pathFlow;
    } 
    
    for (int i = 0; i < V; i++) {
        free(residualGraph[i]);
    } free(residualGraph);
    free(parent);
    
    return maxFlow;
}

int main (void) {
    cout << "Enter the number of vertices: ";
    cin >> V;
    
    int** graph = (int**) malloc(V * sizeof(int*));
    for (int i = 0; i < V; i++) {
        graph[i] = (int*) calloc(V, sizeof(int));
    }

    cout << "Enter the values for the graph:-\n";
    for (int u = 0; u < V; u++) {
        for (int v = 0; v < V; v++)
            cin >> graph[u][v];
    }

    int maxFlow = findMaxFlow(graph, 0, V - 1);
    cout << "Maximum flow: " << maxFlow << endl;
}