"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re

cpf = '444.812.620-01'
cpf_formatado = re.sub(
    r'[^0-9]',
    '',
    cpf
)

# Calculo do primeiro digito
soma = 0
mult = 10
for numero in cpf_formatado[:9]:
    soma += int(numero) * mult
    mult -= 1
resultado_1 = (soma * 10) % 11 

primeiro_digito = 0 if resultado_1 > 9 else resultado_1
print('Primeiro Digito:', primeiro_digito)

# Calculo do segundo digito (precisa do primeiro digito e a variavel "mult" começa em 11)
soma = 0
mult = 11
for numero in cpf_formatado[:10]:
    soma += int(numero) * mult
    mult -= 1
resultado_2 = (soma * 10) % 11 

segundo_digito = 0 if resultado_2 > 9 else resultado_2
print('Segundo Digito:', segundo_digito)

if f'{cpf_formatado[:9]}{primeiro_digito}{segundo_digito}' == cpf_formatado:
    print(f'O CPF {cpf_formatado} é válido')
