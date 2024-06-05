#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celcius = float(input('Insira a temperatura em Celsius: '))

fahrenheit = (celcius * 9/5) + 32

print(f'A temperatura {celcius:.1f}ºC convertido para Fahrenheit {fahrenheit:.1f}ºF')
