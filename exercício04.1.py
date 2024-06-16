# Verificador de Vogais: Crie um programa que verifique se uma letra (informada pelo usuário) é uma vogal ou consoante.

letra = input("Digite a letra que deseja verificar: ").lower()

if letra in "aeiou":
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra é uma consoante.")