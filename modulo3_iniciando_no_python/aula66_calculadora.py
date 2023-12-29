# Calculadora com while

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if not numeros_validos:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = ['+', '-', '/', '*']

    if operador in operadores_permitidos:
        print('Resultado:')
        if operador == '+':
            print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
        elif operador == '-':
            print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
        elif operador == '/':
            print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
        elif operador == '*':
            print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
        else:
            print('não deveria chegar aqui')
    else:
        print('Operador inválido. Digite uma das opções.')

    # Opção para o usuário sair.
    if input('Quer sair? [s]im: ').lower().startswith('s'):
        break