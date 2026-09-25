import sys
from src.dados import ler_dados, distancia, monta_matriz_d
dados = ler_dados("dados/" + sys.argv[1])
d = monta_matriz_d(dados)