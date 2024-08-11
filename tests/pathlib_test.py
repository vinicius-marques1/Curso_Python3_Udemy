from pathlib import Path

path = Path('modulo7_pyside6_interface_grafica')

files = path.rglob('*.py')

list_of_files = list(files)
for f in list_of_files:
    print(f.name)

print(list_of_files)
