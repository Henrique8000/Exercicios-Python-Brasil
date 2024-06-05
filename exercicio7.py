#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
base = int(input('Insira o comprimento da base em cm: '))
altura = int(input('Agora insira a altura em cm: '))

a = base * altura

dobro_a = a * 2

print(f'A área do quadrado é {a}cm e o dobro dessa área é {dobro_a}')

