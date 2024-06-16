# Verificador de Dia da Semana: Escreva um programa que receba um número de 1 a 7 e exiba o dia da semana correspondente
# (1 - Domingo, 2 - Segunda, etc.). Utilize match-case para fazer a correspondência.

numero = int(input("Digite um número de 1 a 7: "))

match numero:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido. Por favor, digite um número de 1 a 7.")