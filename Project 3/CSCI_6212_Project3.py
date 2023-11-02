from collections import defaultdict
import random
import time

# Start measuring the execution time
begin = time.time_ns()

# Function to generate a random graph
def generate_graph(num_nodes, num_edges_perNode):
    G = defaultdict(list)
    nodes = list(range(1, num_nodes + 1))   # Create a list of nodes
    random.shuffle(nodes)  # Shuffle the list of nodes to randomize node selection

    while len(nodes) > 1:
        node = nodes.pop(0)  # Take the first node from the shuffled list
        edges = random.sample(nodes, min(num_edges_perNode, len(nodes)))  # Randomly select other nodes to connect to
        G[node] = edges  # Connect the selected nodes to the current node
    return G

# Function to check for biconnectivity and find articulation points in the graph
def Biconnectivity(G):
    def DFS(node):
        nonlocal num
        DFN[node] = num
        L[node] = num
        num += 1
        T.append(node)

        for neighbor in G[node]:
            if neighbor not in DFN:
                Parent[neighbor] = node
                DFS(neighbor)
                L[node] = min(L[node], L[neighbor] if neighbor in L else float('inf'))
            elif neighbor != Parent[node] and DFN[neighbor] < DFN[node]:
                L[node] = min(L[node], DFN[neighbor])

        if L[node] >= DFN[node] and node != s:
            articulation_points.add(node)

    T = []
    num = 1
    DFN = {}
    L = {}
    Parent = {}
    articulation_points = set()
    s = next(iter(G))  # Choose an unvisited node as the starting point
    L[s] = DFN[s] = num
    num += 1
    T.append(s)

    while T:
        x = T[-1]
        unvisited_neighbor = None
        for neighbor in G[x]:
            if neighbor not in DFN:
                unvisited_neighbor = neighbor
                break

        if unvisited_neighbor is not None:
            DFN[unvisited_neighbor] = num
            num += 1
            Parent[unvisited_neighbor] = x
            L[unvisited_neighbor] = DFN[unvisited_neighbor]
            T.append(unvisited_neighbor)
        else:
            T.pop()
            for neighbor in G[x]:
                if neighbor != Parent.get(x) and DFN[neighbor] < DFN[x]:
                    L[x] = min(L[x], DFN[neighbor])
                elif x == Parent.get(neighbor):
                    L[x] = min(L[x], L[neighbor] if neighbor in L else float('inf'))

            if x != s:
                if L[x] >= DFN[x]:
                    articulation_points.add(x)

    return not bool(articulation_points), articulation_points

''' 
# Generate a random graph with 400 nodes and up to 200 edges per node
Project Input Values
N:- 10,  V:- 5    
N:- 50,  V:- 25      
N:- 75,  V:- 35
N:- 100, V:- 50     
N:- 300, V:- 150  
N:- 400, V:- 200  
'''
num_nodes = 400
num_edges_perNode = 200
random_graph = generate_graph(num_nodes, num_edges_perNode)

# Check for biconnectivity and find articulation points in the graph
is_biconnected, articulation_points = Biconnectivity(random_graph)

# Print the results
if is_biconnected:
    print("The random graph is biconnected.")
else:
    print("The random graph is not biconnected. Articulation points:", articulation_points)

# End measuring the execution time
end = time.time_ns()
print("Execution Time", end - begin, "ns")
