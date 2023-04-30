menu = '''
    [d] Depositar
    [s] Saquar
    [e] Extrato
    [q] Sair
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao =input(menu)


    if opcao == 'd':
        deposito = float(input("Informe o valor do deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Déposito R$: {deposito:.2f}\n"
        else:
            print("Operação inválida, por favor digite valores positivos e não nulos.")
    elif opcao == 's':
        saque = float(input("Informe o valor do saque: "))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Aprovação falhou, você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Não é possível aprovar, limite excedido.")
        elif excedeu_saques:
            print("Não é possível aprovar, limite de saques excedidos.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque R$: {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 'e':
        print("\n******************** Extrato ********************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo R$: {saldo:.2f}\n")
        print("***************************************************")
    elif opcao == 'q':
        break
    else:
        print("Operação inválida, por favor selecine novamente a operação desejada.")
