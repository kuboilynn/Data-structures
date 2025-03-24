'''********GROUP P********
MUTEBI STUART 24/U/25953/PS
CHEBOSIS LYNN KUBOI 24/U/04567/EVE
AROBA JOSEPH 24/U/03646/EVE
MUHEREZA PIUS 24/U/071001/EVE
MUKISA MARK 24/U/24248/PSA'''


import numpy as np
from sklearn.manifold import MDS
import random

# Adjacency matrix from the previous problem
distance = [
    [0, 12, 10, 0, 0, 0, 12],  # City 1 to others
    [12, 0, 8, 12, 0, 0, 0],    # City 2 to others
    [10, 8, 0, 11, 3, 0, 9],    # City 3 to others
    [0, 12, 11, 0, 11, 10, 0],  # City 4 to others
    [0, 0, 3, 11, 0, 6, 7],    # City 5 to others
    [0, 0, 0, 10, 6, 0, 9],    # City 6 to others
    [12, 0, 9, 0, 7, 9, 0]     # City 7 to others
]

N = len(distance)  # Number of cities (7)

# Replace 0s with a large value for MDS (except self-loops)
INF = 9999
dist_matrix = np.array(distance)
for i in range(N):
    for j in range(N):
        if dist_matrix[i][j] == 0 and i != j:
            dist_matrix[i][j] = INF

# Use Multidimensional Scaling to get 2D coordinates for cities
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
city_coords = mds.fit_transform(dist_matrix)

# SOM Parameters
num_neurons = 3 * N  # 21 neurons
eta_0 = 0.1  # Initial learning rate
sigma_0 = num_neurons / 2  # Initial neighborhood radius
tau = 1000  # Time constant for decay
max_iterations = 10000  # Number of iterations

# Initialize neurons on a unit circle
neurons = np.zeros((num_neurons, 2))
for i in range(num_neurons):
    angle = 2 * np.pi * i / num_neurons
    neurons[i] = [np.cos(angle), np.sin(angle)]

# SOM Training
for t in range(max_iterations):
    # Update learning rate and neighborhood radius
    eta = eta_0 * np.exp(-t / tau)
    sigma = sigma_0 * np.exp(-t / tau)

    # Randomly select a city
    city_idx = random.randint(0, N - 1)
    city = city_coords[city_idx]

    # Find the winning neuron
    distances = np.linalg.norm(neurons - city, axis=1)
    winner = np.argmin(distances)

    # Update all neurons
    for i in range(num_neurons):
        # Distance on the ring (shortest path)
        dist_on_ring = min(abs(i - winner), num_neurons - abs(i - winner))

        # Neighborhood function
        h = np.exp(-dist_on_ring**2 / (2 * sigma**2))

        # Update weights
        neurons[i] += eta * h * (city - neurons[i])

# Form the tour
city_to_neuron = []
for city_idx in range(N):
    city = city_coords[city_idx]
    distances = np.linalg.norm(neurons - city, axis=1)
    closest_neuron = np.argmin(distances)
    city_to_neuron.append((closest_neuron, city_idx))

# Sort by neuron index to get the tour
city_to_neuron.sort()
tour = [pair[1] for pair in city_to_neuron]  # Extract city indices

# Ensure the tour starts and ends at City 1 (index 0)
start_idx = tour.index(0)
tour = tour[start_idx:] + tour[:start_idx] + [0]  # Rotate to start at 0, add 0 at the end

# Convert to city numbers (1-based)
tour_cities = [city + 1 for city in tour]

# Compute total distance
total_distance = 0
for i in range(len(tour) - 1):
    city1, city2 = tour[i], tour[i + 1]
    total_distance += distance[city1][city2]

# Print the result
print("SOM Route:", " -> ".join(map(str, tour_cities)))
print("Total Distance:", total_distance)
