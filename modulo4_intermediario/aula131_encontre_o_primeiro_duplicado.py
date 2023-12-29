"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]

def achar_primeiro_numero_repetido(lista: list):
    numero_vistos = set()
    for num in lista:
        if num in numero_vistos:
            return num
        numero_vistos.add(num)
    return -1


# Exercicio EXTRA
# Achar o número que tem mais de uma ocorrencia e que aparece primeiro na lista
def achar_primeiro_numero_que_acore_na_lista_e_e_repetido(lista: list):
    num_vistos = []
    repetidos = set()
    for item in lista:
        if item in num_vistos:
            repetidos.add(item)
        else:
            num_vistos.append(item)
    
    if not repetidos:
        return -1
    
    menor_index = len(num_vistos) - 1 
    for item in repetidos:
        if num_vistos.index(item) < menor_index:
            menor_index = num_vistos.index(item)
    return num_vistos[menor_index]


# Mostrando o resultado das funções para cada lista
for lista in lista_de_listas_de_inteiros:
    print(lista)
    print(f'Primeiro número repetido: {achar_primeiro_numero_repetido(lista)}')
    print(
        'Primeiro número que aparece na lista e tem repetições:',
        achar_primeiro_numero_que_acore_na_lista_e_e_repetido(lista)
    )
    print()
