import tsplib95
from scipy.spatial.distance import cdist

dados = {
    "berlin52": tsplib95.load("dados/berlin52.tsp").node_coords,
    "ch150": tsplib95.load("dados/ch150.tsp").node_coords,
    "kroA100": tsplib95.load("dados/kroA100.tsp").node_coords,
    "kroB200": tsplib95.load("dados/kroB200.tsp").node_coords,
}
cidade = list(dados.values())

#definir cidade inicial, estolhe o ponto mais próximo do ponto inicial e assim por diante.
#deslocamento de [i] para [j] d[i][j]


#Cidade mais próxima da atual
def distancia_caminho(caminho, coordenadas):
    total = 0

    for origem, destino in zip(caminho, caminho[1:]):
        total += cdist(
            [coordenadas[origem]],
            [coordenadas[destino]],
            metric="euclidean",
        )[0][0]

    return total
    
def modelo_vizinho(inicio, coordenadas):
    caminho = [inicio]
    visitadas = {inicio}
    atual = coordenadas[inicio]

    while len(visitadas) < len(coordenadas):
        menor = float("inf")
        cidade_proxima = None

        for cidade, coordenada in coordenadas.items():
            if cidade in visitadas:
                continue

            distancia = cdist([atual], [coordenada], 'euclidean')[0][0]

            if distancia < menor:
                menor = distancia
                cidade_proxima = cidade

        caminho.append(cidade_proxima)
        visitadas.add(cidade_proxima)
        atual = coordenadas[cidade_proxima]

    caminho.append(inicio)

    return caminho

def vizinho_mais_proximo_multistart(coordenadas):
    melhor_caminho = None
    melhor_distancia = float("inf")

    for inicio in coordenadas:
        caminho = modelo_vizinho(inicio, coordenadas)
        distancia = distancia_caminho(caminho, coordenadas)

        if distancia < melhor_distancia:
            melhor_caminho = caminho
            melhor_distancia = distancia
    return  int(melhor_distancia)


teste1 = vizinho_mais_proximo_multistart(dados["berlin52"])
teste2 = vizinho_mais_proximo_multistart(dados["ch150"])
teste3 = vizinho_mais_proximo_multistart(dados["kroA100"])
teste4 = vizinho_mais_proximo_multistart(dados["kroB200"])
print(teste1)
print(teste2)
print(teste3)
print(teste4)