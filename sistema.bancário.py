codigos_conta = []
saldos = []

for n in range(2):
    codigo_conta = int(input("Digite o código da sua conta: "))
    codigos_conta.append(codigo_conta)
    saldo_conta = float(input("Digite o valor do saldo da conta:R$"))
    saldos.append(saldo_conta)

print("SERVIÇOS:")
print("1. Depósito")
print("2. Realizar Saque")
print("3. Consultar ativo bancário")
print("4. Finalizar Programa")

escolha_do_menu = int(input("Digite uma opção acima: "))

#Deposito
if escolha_do_menu == 1:
    codigo_conta = int(input("Digite o código da sua conta: "))
    codigos_conta.append(codigo_conta)
    
    if codigo_conta in codigos_conta:
        indice_conta = codigos_conta.index(codigo_conta)
        valor_de_deposito = float(input("Digite a quantia que deseja depositar:R$"))
        saldos[indice_conta] += valor_de_deposito
        print("O valor que está na conta após o depósito é de: ", saldos[indice_conta])

#Saque
elif escolha_do_menu == 2:
    codigo_conta = int(input("Digite o código da sua conta: "))
    codigos_conta.append(codigo_conta)

    if codigo_conta in codigos_conta:
        indice_conta = codigos_conta.index(codigo_conta)
        valor_de_saque = float(input("Digite o valor que você deseja sacar:R$"))
        saldos[indice_conta] -= valor_de_saque
        if valor_de_saque > saldo_conta:
            print("Saldo insuficiente para realizar esse saque!")
        else:    
            print("O valor restante na sua conta após o saque efetuado é de:R$", saldos[indice_conta])

#Somatório
elif escolha_do_menu == 3:
    soma_dos_saldos = sum(saldos)
    print("A soma de todos os saldos das contasa é de:R$", soma_dos_saldos)

#Finalizar Programa
elif escolha_do_menu == 4:
    print("----------Programa Finalizado----------")

else: 
    print("Digite um número válido !!!")

    

    
