print('Bem vindo a ilha do tesouro!')
escolha = input('Faça sua escolhas, direita ou esquerda: ')


if escolha.lower() == 'direita':
    print('Você morreu meu amigo!')
else:
    print(f'Muito bem! Faça uma nova escolha.')
    escolha2 = input('Deseja lutar contra leões ou aranhas? [L ou A]')
    if escolha2.upper() == 'L':
        print('Você morreu meu amigo!')
    else:
        print('Você localizou o tesouro!')