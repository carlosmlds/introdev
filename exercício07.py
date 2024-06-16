# #Gerenciar um estoque para a empresa U não é complicado, mas ele te pediu para desenvolver um programa para realizar
# esta tarefa. Ela precisa que o usuário informe a quantidade máxima e mínima do estoque do produto X, e também a
# quantidade real existente no estoque. Por fim, o programa deve responder se é necessário adquirir mais produtos,
# comparando o estoque real com a média entre valor máximo e mínimo.
# a. se o estoque real estiver abaixo da média, informar a necessidade de compra;
# b. se estiver acima da média informar que não precisa adquirir novos produtos;
# c. se estiver na média, informa que em breve será necessária nova aquisição de produtos;

quantidade_maxima = int(input("Digite a quantidade máxima do estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima do estoque: "))
quantidade_real = int(input("Digite a quantidade real do estoque: "))
media_estoque = (quantidade_maxima + quantidade_minima) / 2

if quantidade_real < media_estoque:
    print("Necessário adquirir mais produtos.")
elif quantidade_real > media_estoque:
    print("Não é necessário adquirir mais produtos.")
else:
    print("Em breve será necessária nova aquisição de produtos.")

print(f"A média entre a quantidade máxima e mínima do estoque é: {media_estoque:.2f}")