from random import choice

pedra = """
     _______
 ---'   ____)
       (_____)
       (_____)
       (____)
 ---.__(___)
"""

papel = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

opcoes_de_jogo = ['Pedra', 'Papel', 'Tesoura']
desenhos = [pedra, papel, tesoura]
continuar_jogando = True

if __name__ == '__main__':
    while continuar_jogando:
        print("Escolha uma opção:")
        for i, opcao in enumerate(opcoes_de_jogo):
            print(f'{i}: {opcao}')

        escolha = input("Digite o número da sua escolha: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha in [0, 1, 2]:
                print(f'Sua escolha: \n{desenhos[escolha]}')
                escolha_robo = choice(desenhos)
                print(f'Escolha do robô: \n{escolha_robo}')

                if escolha == 0 and escolha_robo == pedra or escolha == 1 and escolha_robo == tesoura or escolha == 2 and escolha_robo == tesoura:
                    print(f'Você ganhou com {opcoes_de_jogo[escolha]} contra {opcoes_de_jogo[opcoes_de_jogo.index("Tesoura")]}!')
                elif escolha == 0 and escolha_robo == tesoura or escolha == 1 and escolha_robo == pedra or escolha == 2 and escolha_robo == papel:
                    print(f'Você ganhou com {opcoes_de_jogo[escolha]} contra {opcoes_de_jogo[opcoes_de_jogo.index("Papel")]}!')
                elif escolha == 0 and escolha_robo == papel or escolha == 1 and escolha_robo == tesoura or escolha == 2 and escolha_robo == papel:
                    print(f'Você ganhou com {opcoes_de_jogo[escolha]} contra {opcoes_de_jogo[opcoes_de_jogo.index("Papel")]}!')
                else:
                    print('Empate!')
            else:
                print('Escolha inválida. Tente novamente.')
        else:
            print('Escolha inválida. Tente novamente.')

        deseja_continuar = input('Deseja continuar jogando? (S/N): ').lower()
        if deseja_continuar != 's':
            continuar_jogando = False
