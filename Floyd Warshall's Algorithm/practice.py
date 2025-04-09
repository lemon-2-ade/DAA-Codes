from typing import List, Tuple

global V
V = 4

def floyd_warshall(dist: List[List[int]], n: int):

    pi = [[ 'NIL' ] * n for i in range(n)]

    for i in range(n):
        for j in range(n):

            if dist[i][j] == 0 or dist[i][j] == 999:
                continue

            if dist[i][j] != 999:
                pi[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):

                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pi[i][j] = pi[k][j]
    
    for row in dist:
        print(" ".join(map(str, row)))
    
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
    
    print("\nShortest paths between every pair of vertices:")
    for i in range(n):
        for j in range(n):
            
            if i == j:
                continue
            
            print(f"Shortest path from node {i} to node {j}: ", end="")
            reconstructed_path(pi, i, j)
                
if __name__ == '__main__':

    graph = [ list(map(int, input().split())) for i in range(V) ]
    floyd_warshall(graph, V)