# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(num: int):
    def multiplica(n):
        return num * n
    return multiplica

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadruplica = criar_multiplicador(4)

print(
    duplica(10),
    triplica(10),
    quadruplica(10)
)