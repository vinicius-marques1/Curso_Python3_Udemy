""" EX1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# # Solução 1
# while True:
#     numero = input('Digite um número inteiro: ')
#     if numero.isdigit():
#         numero_int = int(numero)
#         if numero_int % 2 == 0:
#             print(f'O numero {numero_int} é par')
#         else:
#             print(f'O número {numero_int} é impar')
#         break
#     else:
#         print('Digite um número!')


# Solução 2
while True:
    numero = input('Digite um número inteiro: ')
    try:
        numero_int = float(numero)
        if numero_int % 2 == 0:
            print(f'O numero {numero} é par')
        else:
            print(f'O número {numero} é impar')
        break
    except:
        print('Digite um número!')