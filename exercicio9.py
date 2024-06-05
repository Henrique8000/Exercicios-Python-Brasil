#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = float(input('Digite a temperatura em Fahrenheit: '))

conversao = (f - 32) * 5/9

print(f'{conversao:.0f}C')
