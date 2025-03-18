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
