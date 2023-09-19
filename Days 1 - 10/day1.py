print('Bem vindo ao gerador de nome de bandas.')

cidade = input('Me fale o nome da cidade em que você nasce? ')
animal = input('Infome o nome do seu pet ou que daria a ele? ')

nome_da_banda = f'{cidade.capitalize()} {animal.capitalize()}'
print(f'O nome de sua banda é {nome_da_banda}')