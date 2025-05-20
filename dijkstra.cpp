#include <iostream>
#include <limits>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

vector<int> getShortestPaths (unordered_map<int, vector<pair<int, int>>> graph, int source, int numOfVertices) {
    int INF = numeric_limits<int>::max();
    vector<int> distances(numOfVertices, INF);
    distances[source] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({ distances[source], source });

    while (!pq.empty()) {
        auto [ currDist, node ] = pq.top();
        pq.pop();

        if (currDist > distances[node])
            continue;
        
        for (const auto& [ neighbour, weight ]: graph[node]) {
            if (weight + currDist < distances[neighbour]) {
                distances[neighbour] = weight + currDist;
                pq.push({ distances[neighbour], neighbour });
            }
        }
    } return distances;
}

unordered_map<int, vector<pair<int, int>>> constructGraph (vector<tuple<int, int, int>> edges, int numOfVertices) {
    unordered_map<int, vector<pair<int, int>>> graph;

    for (const auto& edge: edges) {
        int u = get<0>(edge), v = get<1>(edge);
        int weight = get<2>(edge);
        graph[u].push_back({ v, weight });   
    } return graph;
}