from typing import List, Tuple

global V

def floyd_warshall(dist: List[List[int]]):
    pi = [['NIL'] * V for u in range(V)]
    INF = 999

    for u in range(V):
        for v in range(V):
            if 0 < dist[u][v] < INF:
                pi[u][v] = u
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pi[i][j] = pi[k][j]
    
    def reconstructed_path(pi: List[List[int]], start: int, end: int):
        if pi[start][end] == 'NIL':
            return [ start ] if start == end else None
        
        path = [ end ]
        while end != start:
            end = pi[start][end]

            if end == 'NIL':
                return None
            path.append(end)
        
        path = list(reversed(path))
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            else:
                print(path[i], end=" -> ")

    print("Shortest path from every pair of vertices:-")
    for u in range(V):
        for v in range(V):
            if 0 < dist[u][v] < INF:
                print(f"Shortest path from {u} to {v}: ", end=" ")
                reconstructed_path(pi, u, v)
                
if __name__ == '__main__':

    V = int(input("Enter the number of vertices:-"))
    print("Enter the values for adjacency matrix:-")
    graph = [ list(map(int, input().split())) for i in range(V) ]

    floyd_warshall(graph)