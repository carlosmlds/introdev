#Verificador de Número Par ou Ímpar: Crie um programa que verifique se um número (informado pelo usuário) é par ou ímpar.

numero = int(input("Digite o número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")