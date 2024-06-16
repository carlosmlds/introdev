    peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    condicao = "abaixo do peso"
elif imc >= 18.5 and imc < 25:
    condicao = "peso normal"
elif imc >= 25 and imc < 30:
    condicao = "acima do peso"
else:
    condicao = "obeso"

print(f"Seu IMC é: {imc: .2f}")
print(f"Sua condição é: {condicao}")