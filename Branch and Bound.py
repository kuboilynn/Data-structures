'''********GROUP P********
MUTEBI STUART 24/U/25953/PS
CHEBOSIS LYNN KUBOI 24/U/04567/EVE
AROBA JOSEPH 24/U/03646/EVE
MUHEREZA PIUS 24/U/071001/EVE
MUKISA MARK 24/U/24248/PSA'''

import heapq
import copy

# Adjacency matrix 
distance = [
    [0, 12, 10, 0, 0, 0, 12],  # City 1 to others
    [12, 0, 8, 12, 0, 0, 0],   # City 2 to others
    [10, 8, 0, 11, 3, 0, 9],   # City 3 to others
    [0, 12, 11, 0, 11, 10, 0],  # City 4 to others
    [0, 0, 3, 11, 0, 6, 7],    # City 5 to others
    [0, 0, 0, 10, 6, 0, 9],    # City 6 to others
    [12, 0, 9, 0, 7, 9, 0]     # City 7 to others
]

N = len(distance)  # Number of cities (7)

# Replace 0s with infinity for edges that don't exist (except self-loops)
INF = float('inf')
for i in range(N):
    for j in range(N):
        if distance[i][j] == 0 and i != j:
            distance[i][j] = INF

# Class to represent a node in the state space tree
class Node:
    def __init__(self, cost, vertex, path, visited, reduced_matrix):
        self.cost = cost  # Cost of the path so far
        self.vertex = vertex  # Current vertex
        self.path = path  # Path taken so far
        self.visited = visited  # Set of visited vertices
        self.reduced_matrix = reduced_matrix  # Reduced cost matrix
        self.lower_bound = 0  # Lower bound for this node

    def __lt__(self, other):
        return self.lower_bound < other.lower_bound

# Function to compute the initial reduction of the matrix and the lower bound
def reduce_matrix(matrix):
    N = len(matrix)
    reduction_cost = 0
    # Reduce rows
    for i in range(N):
        min_val = min(matrix[i])
        if min_val != INF and min_val != 0:
            reduction_cost += min_val
            for j in range(N):
                if matrix[i][j] != INF:
                    matrix[i][j] -= min_val
    # Reduce columns
    for j in range(N):
        min_val = INF
        for i in range(N):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
        if min_val != INF and min_val != 0:
            reduction_cost += min_val
            for i in range(N):
                if matrix[i][j] != INF:
                    matrix[i][j] -= min_val
    return matrix, reduction_cost

# Function to compute the lower bound for a node
def compute_lower_bound(node, curr_vertex, next_vertex):
    # Create a copy of the reduced matrix
    new_matrix = copy.deepcopy(node.reduced_matrix)
    N = len(new_matrix)

    # Set the row of the current vertex to INF
    for j in range(N):
        new_matrix[curr_vertex][j] = INF
    # Set the column of the next vertex to INF
    for i in range(N):
        new_matrix[i][next_vertex] = INF
    # Prevent returning to the start city until all cities are visited
    if len(node.visited) < N:
        new_matrix[next_vertex][0] = INF
    # Reduce the new matrix
    new_matrix, reduction_cost = reduce_matrix(new_matrix)
    # Lower bound = cost so far + cost to next vertex + reduction cost
    lower_bound = node.cost + distance[curr_vertex][next_vertex] + reduction_cost
    return lower_bound, new_matrix

# Branch and Bound algorithm for TSP
def tsp_branch_and_bound():
    # Step 1: Reduce the initial matrix
    reduced_matrix, initial_cost = reduce_matrix(copy.deepcopy(distance))

    # Step 2: Initialize the priority queue with the starting node (City 1, index 0)
    start_vertex = 0  # City 1
    path = [start_vertex]
    visited = {start_vertex}
    root = Node(0, start_vertex, path, visited, reduced_matrix)
    root.lower_bound = initial_cost

    # Priority queue to store nodes (based on lower bound)
    pq = []
    heapq.heappush(pq, root)
    # Best solution
    best_cost = INF
    best_path = None

    # Step 3: Process nodes in the priority queue
    while pq:
        node = heapq.heappop(pq)
        # If all cities are visited, check the cost to return to the start
        if len(node.visited) == N:
            return_cost = distance[node.vertex][start_vertex]
            if return_cost != INF:
                total_cost = node.cost + return_cost
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = node.path + [start_vertex]
            continue

        # Explore next possible vertices
        curr_vertex = node.vertex
        for next_vertex in range(N):
            if next_vertex not in node.visited and distance[curr_vertex][next_vertex] != INF:
                # Compute the lower bound for this path
                lower_bound, new_matrix = compute_lower_bound(node, curr_vertex, next_vertex)
                # If the lower bound is less than the best cost, explore this path
                if lower_bound < best_cost:
                    new_path = node.path + [next_vertex]
                    new_visited = node.visited | {next_vertex}
                    new_cost = node.cost + distance[curr_vertex][next_vertex]
                    new_node = Node(new_cost, next_vertex, new_path, new_visited, new_matrix)
                    new_node.lower_bound = lower_bound
                    heapq.heappush(pq, new_node)

    return best_path, best_cost

# Run the algorithm
best_path, best_cost = tsp_branch_and_bound()

# Convert path indices to city numbers (index 0 -> City 1, etc.)
best_path = [city + 1 for city in best_path]

# Print the result
print("Optimal Route:", " -> ".join(map(str, best_path)))
print("Total Distance:", best_cost)
