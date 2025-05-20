from collections import deque
from typing import List, Tuple

global V

def contruct_graph(roads: List[Tuple[int]]):
    # constructing the graph from given set of paths
    graph = [[ float('inf') ] * V for i in range(V)]

    for i in range(V):
        graph[i][i] = 0
    
    for u, v, weight in roads:
        graph[u][v] = weight
        graph[v][u] = weight    # for undirected graph
    
    return graph

def print_adjacency_matrix(graph: List[List[int]]):
    # printing the adjacency matrix of the graph
    for row in graph:
        print(' '.join(map(str, row)))

def bfs(graph: List[List[int]], start: int):
    # func. implementing breadth-first search algorithm
    visited = [ False ] * V
    queue = deque([ start ])
    visited[start] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        visited[current] = True

        for v in range(V):
            if 0 < graph[current][v] < float('inf') and not visited[v]:
                queue.append(v)
                visited[v] = True

def dfs(graph: List[List[int]], start: int, visited = None):
    # func. implementing depth-first search algorithm
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')

    for neighbour in range(V):
        if 0 < graph[start][neighbour] < float('inf') and neighbour not in visited:
            dfs(graph, neighbour, visited)

def shortest_paths(graph: List[List[int]], start: int):
    # dijsktra's algorithm for single-source shortest path
    visited = [ False ] * V
    distances = [ float('inf') ] * V
    distances[start] = 0
    
    for _ in range(V):
        min_dist, min_node = float('inf'), -1

        for i in range(V):
            # finding unvisited node with smallest distance
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_node = i
            
        if min_node == -1:
            break   # remaining nodes are unreachable

        visited[min_node] = True

        for neighbour in range(V):
            weight = graph[min_node][neighbour]

            if 0 < weight < float('inf') and not visited[neighbour]:
                distances[neighbour] = min(distances[neighbour], distances[min_node] + weight)
    
    return distances

if __name__ == '__main__':

    V = 9
    roads = [
        (0, 1, 4), (0, 4, 8),
        (1, 2, 8), (1, 4, 11),
        (2, 3, 7), (2, 8, 2), (2, 6, 4),
        (3, 7, 9), (3, 6, 14),
        (4, 8, 7), (4, 5, 1),
        (5, 6, 2), (5, 8, 6),
        (6, 7, 10)
    ]

    graph = contruct_graph(roads)
    
    print("Vertices: ", end='')
    dfs(graph, 0)