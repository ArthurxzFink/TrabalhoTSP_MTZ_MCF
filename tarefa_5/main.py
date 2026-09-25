import sys
from tarefa_5.src.dados import ler_dados

n, cord = ler_dados("dados/" + sys.argv[1])
print(n)
print(cord)