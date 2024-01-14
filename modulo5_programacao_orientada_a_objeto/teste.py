try:
    prin('sdsd')
except Exception as e:
    e.add_note('Meu erro!')
    print(e.__notes__)
    