from amplpy import AMPL
from .dados import ler_dados, monta_matriz_d, distancia

def resolver_tsp(caminho_arquivo):
    n, cord = ler_dados(caminho_arquivo)
    d = monta_matriz_d(cord)
    ampl = AMPL()

    ampl.read(modelo)
    