from graphs_LightningRadeken import sp

def load_graph_from_file(filename):
    with open(filename,"r") as f:
        lines = f.readlines()
    
    n = int(lines[0].strip())
    graph = {i: {} for i in range(n)}

    for line in lines[1:]:
        u, v, w = map(int, line.strip().split())
        graph[u][v] = w
    
    return graph

graph1 = load_graph_from_file("example1.txt")
dist1, path1 = sp.dijkstra(graph1,0)
print("Example1:")
print("Distances:", dist1)
print("Paths:", path1)

graph2 = load_graph_from_file("example2.txt")
dist2, path2 = sp.dijkstra(graph2,0)
print("Example2:")
print("Distances:", dist2)
print("Paths:", path2)

graph3 = load_graph_from_file("example3.txt")
dist3, path3 = sp.dijkstra(graph3,0)
print("Example3:")
print("Distances:", dist3)
print("Paths:", path3)