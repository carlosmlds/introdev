numero_macas = int(input("Digite o número de maças desejadas: "))
preco_unidade = 1.37
preco_desconto = 1.24
if numero_macas >= 12:
    valor_total = numero_macas * preco_desconto
else:
    valor_total = numero_macas * preco_unidade
print(f"O valor total da compra é R${valor_total: .2F}")