import numpy as np
import networkx as nx
from itertools import permutations

def read_matrix_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.strip().split())) for line in lines]
    return np.array(matrix)

def calculate_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]['weight']
    return cost

def traveling_salesman(graph):
    num_nodes = len(graph.nodes)
    all_nodes = set(graph.nodes)
    start_node = 1  # Pradedame nuo mazgo 1

    best_path = None
    best_cost = float('inf')

    # Sugeneruojame visas galimas keliones, kurios prasideda ir baigiasi pirmame mieste
    all_paths = permutations(all_nodes - {start_node})
    for path in all_paths:
        current_path = (start_node,) + path + (start_node,)
        current_cost = calculate_cost(current_path, graph)

        # Atnaujiname geriausią kelią ir sanaudas, jei randame optimalesni varianta
        if current_cost < best_cost:
            best_path = current_path
            best_cost = current_cost

    return best_path, best_cost

def main():
    file_name = 'grafas.txt'  
    adjacency_matrix = read_matrix_from_file(file_name)

    # Grafo sukurimas naudojant networkx
    graph = nx.Graph()
    num_nodes = len(adjacency_matrix)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            graph.add_edge(i + 1, j + 1, weight=adjacency_matrix[i][j])
    
    # Surandame optimalų kelią ir sąnaudas
    optimal_path, optimal_cost = traveling_salesman(graph)

    print("Optimalus Kelias:", optimal_path)
    print("Optimalios Sąnaudos:", optimal_cost)

if __name__ == "__main__":
    main()
