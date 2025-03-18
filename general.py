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

# Implement the nearest neighbor algorithm
def tsp_nearest_neighbor(graph, start=0):
    n = len(graph)  # Number of cities
    visited = [False] * n  # Track visited cities
    route = [start]  # Start from the given city
    total_distance = 0
    
    current = start
    visited[current] = True  # Mark starting city as visited
    
    for _ in range(n - 1):
        nearest_city = None
        min_distance = float('inf')

        # Find the nearest unvisited city
        for city in range(n):
            if not visited[city] and 0 < graph[current][city] < min_distance:
                nearest_city = city
                min_distance = graph[current][city]

        # Move to the nearest city
        if nearest_city is not None:
            route.append(nearest_city)
            visited[nearest_city] = True
            total_distance += min_distance
            current = nearest_city

    # Return to the starting city
    total_distance += graph[current][start]
    route.append(start)

    return route, total_distance


# Run the algorithm on our TSP graph
route, distance = tsp_nearest_neighbor(graph)

# Display results
print("Nearest Neighbor TSP Route:", " -> ".join(str(city + 1) for city in route))
print("Total Distance:", distance)
