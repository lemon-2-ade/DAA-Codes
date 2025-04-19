from typing import List
global V

def dfs(residual_graph: List[List[int]], source: int, sink: int, parent: List[int]):

    visited = [ False ] * V
    stack = []

    visited[source] = True
    stack.append(source)
    parent[source] = -1

    while stack:
        u = stack.pop()

        for v in range(V):
            if not visited[v] and residual_graph[u][v] > 0:
                parent[v] = u

                if v == sink:
                    return True
                
                stack.append(v)
                visited[v] = True
    
    return False

def ford_fulkerson(graph: List[List[int]], source: int, sink: int):

    residual_graph = [[0] * V for v in range(V)]

    for u in range(V):
        for v in range(V):
            residual_graph[u][v] = graph[u][v]

    parent = [-1] * V
    max_flow = 0

    while dfs(residual_graph, source, sink, parent):
        path_flow = float('inf')

        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = parent[v]
        
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow
    
    return max_flow

if __name__ == '__main__':

    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    paths = [tuple(map(int, input().split())) for e in range(E)]

    graph = [[0] * V for v in range(V)]
    for u, v, flow in paths:
        graph[u][v] = flow
    
    max_flow = ford_fulkerson(graph, 0, V - 1)
    print(f"Maximum flow: {max_flow}")