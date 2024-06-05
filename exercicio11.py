#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1_int = int(input('Digite um número inteiro: '))
n2_int = int(input('Digite outro número inteiro: '))
n_real = float(input('Digite um número real: '))

a = (n1_int * 2) * ( n2_int / 2)
b = (n1_int * 3) + n_real
c = n_real ** 3

print(f'{a:.1f}')
print(f'{b:.1f}')
print(f'{c:.1f}')

