# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join(
    '/home',
    'vinic',
    'Udemy',
    'Curso_Python3',
    'modulo6_modulos_python_os_datetime_etc', 
    'exemplo_aula283'
    )

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for arquivo in os.listdir(caminho_completo_pasta):
        print('  ', arquivo)


# listando o que existe nesse diretório
print()
print(
    *os.listdir('/home/vinic/Udemy/Curso_Python3/modulo6_modulos_python_os_datetime_etc'), sep='\n'
)