"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva
o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.
"""


def main():

    pop_a = int(input("População do lugar A: ").replace(".", ""))
    pop_b = int(input("População do lugar B:").replace(".", ""))
    taxa_a = float(input("\nTaxa de crescimento da população A: "))
    taxa_b = float(input("\nTaxa de crescimento da população B: "))

    qtd_anos = conta_tempo(pop_a, pop_b, taxa_a, taxa_b)

    print(f"Em {qtd_anos} anos, a população A irá passar a populção B em números")


def conta_tempo(a, b, tax_a, tax_b):
    ano = 0
    while a <= b:
        a += a * tax_a / 100
        b += b * tax_b / 100
        ano += 1

    return ano


main()
