#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
ganho_horas = float(input('Quanto você ganha por hora? '))
n_horas = float(input('Quantas horas você trabalhou esse mês? '))

calc_tsm = ganho_horas * n_horas

print(f'{calc_tsm:.2f}')



