import tsplib95
from scipy.spatial.distance import cdist

dados = tsplib95.load("dados/berlin52.tsp")


#definir cidade inicial, estolhe o ponto mais próximo do ponto inicial e assim por diante.
#deslocamento de [i] para [j] d[i][j]


#Cidade mais próxima da atual
def vizinho_mais_proximo(inicial, coordenadas):
    menor = float("inf")
    cidade = None
    for cidade, coordenada in coordenadas.items():
        if inicial != coordenada:
            if cdist([inicial], [coordenada],'euclidean') < menor:
                menor = cdist([inicial], [coordenada],'euclidean')
                cidade = coordenada


    return cidade

#caminho sempre pela distância mais próxima
def modelo_vizinho(inicio, coordenadas):
    caminho = []
    caminho.append(inicio)

    for cidade, coordenada in coordenadas.items():
        if inicio != coordenada:
            caminho.append(vizinho_mais_proximo(inicio, coordenadas))
    return caminho


menor = vizinho_mais_proximo(dados.node_coords[1], dados.node_coords)
caminho = modelo_vizinho(dados.node_coords[1], dados.node_coords)
print(menor)
print(caminho)
