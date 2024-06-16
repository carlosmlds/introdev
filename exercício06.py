# Um programa é necessário para habilitar o funcionamento de uma conta corrente em um banco digital. O programa deve
# permitir ao cliente iniciar com um depósito, realizar um saque, e ao final verificar se o saldo da conta está positivo ou
# negativo. Se negativo, informa qual o valor será necessário para quitar o débito.

deposito_inicial = float(input("Digite o valor inicial de depósito: R$"))
valor_saque = float(input("Digite o valor de saque: R$"))
saldo_final = deposito_inicial - valor_saque

if saldo_final >=0:
    print(f"O saldo da conta está positivo: R${saldo_final:.2f}")
else:
    valor_quitacao = abs(saldo_final)
    print(f"O saldo da conta está negativado: R${saldo_final:.2f}")
    print(f"Será necessário depositar R${valor_quitacao:.2f} para quitar o débito.")