print(f'Bem vindo ao calculador de gorjetas.')
valor_final_conta = float(input('Informe o valor total de sua conta: '))
porcentagem_da_gorjeta  = float(input('Informe quantos /% deseja deixar de gorjeta? '))
quantidade_de_pessoas = int(input('Quantas pessoas para dividr a conta? '))

valor_com_reajuste = valor_final_conta + (valor_final_conta * porcentagem_da_gorjeta / 100)
valor_para_cada = valor_final_conta / quantidade_de_pessoas

print(f'Cada pessoa deve pagar R$ {valor_para_cada:.2f}')