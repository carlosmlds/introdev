numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite a operação aritmética desejada (+, -, *, /, **): ")
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero não permitida."
elif operacao == "**":
    resultado = numero1 ** numero2
else:
    resultado = "Erro: Operação inválida."

print(f"O resultado da operação {numero1}{operacao}{numero2} é: {resultado}")