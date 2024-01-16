# Classes decoradoras (Decorator classes)

# Desse jeito é a instancia da classe que é o decorator
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(2)
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)



# Dessa forma é a classe que é o decorator
# class Multiplicar:
#     def __init__(self, fun):
#         self.func = fun
#         self._multiplicador = 2

#     def __call__(self, *args):
#         # print(args)
#         resultado = self.func(*args)
#         return resultado * self._multiplicador


# @Multiplicar
# def soma(x, y):
#     return x + y


# dois_mais_quatro = soma(2, 4)
# print(dois_mais_quatro)
