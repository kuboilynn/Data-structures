import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom

# City coordinates (arbitrary positions for SOM to learn)
city_positions = np.array([
    [0.2, 0.8],  # City 1
    [0.6, 0.9],  # City 2
    [0.8, 0.5],  # City 3
    [0.5, 0.2],  # City 4
    [0.2, 0.3],  # City 5
    [0.1, 0.6],  # City 6
    [0.4, 0.7],  # City 7
])

num_neurons = len(city_positions)  # Number of neurons = number of cities
som = MiniSom(1, num_neurons, 2, sigma=1.0, learning_rate=0.5)

# Initialize neurons in a circular shape
theta = np.linspace(0, 2 * np.pi, num_neurons, endpoint=False)
neuron_positions = np.column_stack((np.cos(theta), np.sin(theta)))

som.random_weights_init(neuron_positions)

# Train SOM
som.train(city_positions, 10000)  # Train for 10,000 iterations

# Get the neuron activation order
winner_neurons = np.array([som.winner(city) for city in city_positions])
route_order = np.argsort(winner_neurons[:, 1])  # Sort by y-coordinates

# Convert to city index order
tsp_route = list(route_order) + [route_order[0]]  # Return to start

# Plot results
plt.figure(figsize=(6, 6))
plt.scatter(city_positions[:, 0], city_positions[:, 1], label="Cities", color="red")
plt.plot(city_positions[tsp_route, 0], city_positions[tsp_route, 1], marker='o', linestyle='-', color="blue", label="SOM Route")
plt.legend()
plt.title("TSP Solution using SOM")
plt.show()

# Print the TSP route
print("SOM TSP Route:", " -> ".join(str(city + 1) for city in tsp_route))

