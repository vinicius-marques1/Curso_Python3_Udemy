# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def unir_listas(x, y):
    # Solução com função zip (principal)
    return list(zip(x, y)) 

    # Solução com zip_longest
    # return list(zip_longest(x, y, fillvalue='Sem cidade'))

    # Solução com list comprehension
    # intervalo_maximo = min(len(x), len(y))
    # return [
    #     (x[i], y[i]) for i in range(intervalo_maximo)
    # ]

print(unir_listas(cidades, estados))
