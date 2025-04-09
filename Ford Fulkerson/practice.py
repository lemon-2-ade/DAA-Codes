from typing import List

global V
V = 6

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
    flow_graph = [[0] * V for v in range(V)]

    for u in range(V):
        for v in range(V):
            residual_graph[u][v] = graph[u][v]
    
    parent = [-1] * V
    max_flow = 0
    
    while dfs(residual_graph, source, sink, parent):
        path_flow = float('inf')

        v = sink    # to obtain the minimum bottleneck value
        while v != source:
            u = parent[v]
            if residual_graph[u][v] < path_flow:
                path_flow = residual_graph[u][v]
            v = parent[v]

        v = sink    # updating the residual network
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            flow_graph[u][v] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow, flow_graph

if __name__ == '__main__':
    graph = [
        [ 0, 10, 12, 0, 0, 0 ],
        [ 0, 0, 11, 13, 0, 0 ],
        [ 0, 4, 0, 0, 14, 0 ],
        [ 0, 0, 9, 0, 0, 20 ],
        [ 0, 0, 0, 7, 0, 4 ],
        [ 0, 0, 0, 0, 0, 0 ]

    ]
    source, sink = 0, 5

    max_flow, flow_graph = ford_fulkerson(graph, source, sink)
    print(f"Maximum flow: {max_flow}\n")

    for u in range(V):
        for v in range(V):
            if flow_graph[u][v] > 0:
                print(f"Edge ({u} -> {v}): {flow_graph[u][v]}")