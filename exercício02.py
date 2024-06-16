#Conversor de Temperatura: Faça um programa que converta temperaturas entre Celsius e Fahrenheit. O usuário deve
# informar a temperatura e a escala de origem, e o programa deve calcular e exibir a temperatura na outra escala.

temperatura = float(input("Digite o valor da temperatura (apenas o número): "))
escala = input("Digite a escala de origem da temperatura (C ou F): ").upper()

if escala == "C":
    resultado = (temperatura * 9/5) +32
    print(f"{temperatura}{escala} em Fahrenheit é {resultado}.")
elif escala == "F":
    resultado = (temperatura - 32) / 1.8
    print(f"{temperatura}{escala} em Celsius é {resultado}")
else:
    print("Escala inválida")