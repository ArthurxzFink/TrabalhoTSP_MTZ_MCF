def ler_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        cord = {}
        lendo_cord = False

        for linha in arquivo:
            linha_limpa = linha.strip()
            linha_upper = linha_limpa.upper()

            if linha_upper.startswith("NODE_COORD_SECTION"):
                lendo_cord = True
                continue

            if linha_upper.startswith("EOF"):
                break

            if lendo_cord:
                partes = linha_limpa.split()
                if len(partes) >= 3:
                    id_cidade = int(partes[0])
                    x = float(partes[1])
                    y = float(partes[2])
                    cord[id_cidade] = (x, y)
        
        n = len(cord)
   

    return n, cord

def distancia(p1, p2):
    import math
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def monta_matriz_d(cord):
    cidades = sorted(cord)
    n = len(cidades)

    d = [[0.0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in cidades:
        for j in cidades:
            if i == j:
                d[i][j] = 0.0
            else:
                d[i][j] = distancia(cord[i], cord[j])

    return d