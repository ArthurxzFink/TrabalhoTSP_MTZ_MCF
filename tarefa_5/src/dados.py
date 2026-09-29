import tsplib95
from scipy.spatial.distance import cdist

dados = {
    "berlin52": tsplib95.load("dados/berlin52.tsp").node_coords,
    "ch150": tsplib95.load("dados/ch150.tsp").node_coords,
    "kroA100": tsplib95.load("dados/kroA100.tsp").node_coords,
    "kroB200": tsplib95.load("dados/kroB200.tsp").node_coords,
}
cidade = list(dados.values())

print(cidade[1])