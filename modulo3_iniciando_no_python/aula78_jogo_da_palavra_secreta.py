import os
# Exercicio do jogo da palavar secreta

palavra_secreta = 'perfume'
letras_acertadas = []
numeros_tentativas = 0

print('Bem vindo ao jogo da palavra secreta!')
print('Você tem 6 tentativas.')
while numeros_tentativas < 6:
    letra_digitada = input('Digite uma letra: ')
    numeros_tentativas += 1

    os.system('clear')
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas.append(letra_digitada)
    else:
        print(f'A letra "{letra_digitada}" não está na palavra secreta.')
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Você ganhou! Parabéns!')
        print('A palavra era:', palavra_secreta)
        print('Números de tentativas:', numeros_tentativas)
        break

if numeros_tentativas == 6:
    print('Tentativas:', numeros_tentativas)
    print('Suas tentativas acabaram!')
