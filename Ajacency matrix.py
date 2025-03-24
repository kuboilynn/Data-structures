'''********GROUP P********
MUTEBI STUART 24/U/25953/PS
CHEBOSIS LYNN KUBOI 24/U/04567/EVE
AROBA JOSEPH 24/U/03646/EVE
MUHEREZA PIUS 24/U/071001/EVE
MUKISA MARK 24/U/24248/PSA'''

#7 cities (City 1= index 0,City 2=index1 etc)
distance = [
    [0,12,10,0,0,0,12], #city 1 to others
    [12,0,8,12,0,0,0], #city 2 to others
    [10,8,0,11,3,0,9], #city 3 to others
    [0,12,11,0,11,10,0], #city 4 to others
    [0,0,3,11,0,6,7], #city 5 to others
    [0,0,0,10,6,0,9], #city 6 to others
    [12,0,9,0,7,9,0] #city 7 to others
    
]
cities = ["1", "2", "3", "4", "5", "6", "7"]
# Function to print the graph in a readable way
def print_graph(distance, cities):
    print("   ", "  ".join(cities))
    for i, row in enumerate(distance):
        print(cities[i], row)

# Display the adjacency matrix
print_graph(distance, cities)