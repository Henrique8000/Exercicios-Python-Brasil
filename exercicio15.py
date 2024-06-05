'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''
import os

ghoras = float(input('Quanto você ganha por hora? '))
nhoras = float(input('Quantas horas você trabalhou no mês? '))

salario = ghoras * nhoras
ir = (salario * 11) / 100
inss = (salario * 8) / 100
sindi = (salario * 5) / 100
desconto = ir + inss + sindi
s_liquido = salario - desconto

os.system('cls')
print(f'+ Salário Bruto : R${salario:.2f}')
print(f'- IR (11%) : R${ir:.2f}')
print(f'- INSS (8%) : R${inss:.2f}')
print(f'- Sindicato (5%) : R${sindi:.2f}')
print(f'= Salário Liquido com um desconto de R${desconto:.2f} == R${s_liquido:.2f}')
