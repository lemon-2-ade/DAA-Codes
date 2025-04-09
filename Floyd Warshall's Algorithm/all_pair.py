from typing import List, Tuple

def floyd_warshall(roads: List[Tuple[int, int, int]], n: int):

    dist = [[float('inf')] * (n + 1) for i in range(n + 1)]
    pi = [['NIL'] * (n + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for u, v, weight in roads:
        if weight < dist[u][v]:
            dist[u][v] = weight
            pi[u][v] = u
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pi[i][j] = pi[k][j]
    
    print("\nDistance matrix:-")
    for row in dist[1:]:
        print(" ".join(map(str, row[1:])))
    
    print("\nPredecessor matrix:-")
    for row in pi[1:]:
        print(" ".join(map(str, row[1:])))

    return dist, pi

def reconstruct_path(pi: List[List[int]], start: int, end: int):

    if pi[start][end] == 'NIL':
        return [ start ] if start == end else None
    
    path = [ end ]
    while end != start:
        end = pi[start][end]

        if end == 'NIL':
            return None
        path.append(end)
    
    return list(reversed(path))

if __name__ == "__main__":

    vertices = 4
    paths = 6

    roads = [
        (1, 2, 3),
        (1, 4, 5),
        (2, 1, 2),
        (2, 4, 4),
        (3, 2, 1),
        (4, 3, 2)
    ]

    dist, pi = floyd_warshall(roads, vertices)
    start_node, end_node = 4, 1
    
    path = reconstruct_path(pi, start_node, end_node)

    if path:
        print(f"\nShortest path from {start_node} to {end_node}: {path}")
    else:
        print(f"\nNo path found from {start_node} to {end_node}!")