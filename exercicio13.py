#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h = float(input('Insira a sua altura em metros: '))

peso_ideal_m = (72.7 * h) - 58
peso_ideal_f = (62.1 * h) - 44.7

print(f'Caso você seja mulher, o seu peso ideal seria {peso_ideal_f:.1f}kg\nE caso você seja um homem, o seu peso ideal seria: {peso_ideal_m:.1f}kg')
