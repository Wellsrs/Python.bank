menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. Depósitos precisam ser maiores que zero.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        else:
            valor = float(input("Informe o valor do saque: "))
            if valor > saldo:
                print("Saldo insuficiente.")
            elif valor > limite:
                print("O valor do saque excede o limite.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido. Saques precisam ser maiores que zero.")

    elif opcao == "e":
        print("\n====== Extrato ======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=====================")

    elif opcao == "q":
        break
   
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
