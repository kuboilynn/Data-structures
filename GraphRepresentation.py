# Corrected Adjacency Matrix for the given TSP graph
graph = [
    [0, 12, 12, 0, 0, 0, 0],  # City 1
    [12, 0, 10, 8, 12, 0, 0],  # City 2
    [12, 10, 0, 9, 11, 0, 0],  # City 3
    [0, 8, 9, 0, 0, 7, 0],     # City 4
    [0, 12, 11, 0, 0, 10, 0],  # City 5
    [0, 0, 0, 7, 10, 0, 9],    # City 6
    [0, 0, 0, 0, 0, 9, 0],     # City 7
]

cities = ["1", "2", "3", "4", "5", "6", "7"]

# Function to print the graph in a readable way
def print_graph(graph, cities):
    print("   ", "  ".join(cities))
    for i, row in enumerate(graph):
        print(cities[i], row)

# Display the adjacency matrix
print_graph(graph, cities)
