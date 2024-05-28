opcao = -1

saldo = 0
limite_saque = 500
qtd_saques_diario = 3

transacoes_extrato = []

def depositar():
    global saldo
    try: 
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito > 0:    
            saldo += valor_deposito
            transacoes_extrato.append(f"Deposito: R$ {valor_deposito:.2f}")
            print(f'Você depositou R$ {valor_deposito:.2f}, seu saldo atual é de R$ {saldo:.2f}')
        else: 
            print("Digite um valor válido")
    except ValueError:
        print("Digite um valor válido")

def sacar():
    global saldo, qtd_saques_diario
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Saques disponíveis hoje: {qtd_saques_diario}")
    try:
        valor_saque = float(input("Digite o valor de saque que deseja retirar: "))
        if qtd_saques_diario == 0:
            print(":( Limite de saques diários atingido, próximo saque disponível amanhã")
            return
        if valor_saque > 0 and valor_saque <= limite_saque and valor_saque <= saldo and qtd_saques_diario > 0:
            qtd_saques_diario -= 1
            saldo -= valor_saque
            transacoes_extrato.append(f"Saque: R$ {valor_saque:.2f}")

            print(f"Você sacou o valor de R$ {valor_saque:.2f}, e possui o saldo de R$ {saldo:.2f}, (Saques disponíveis hoje: {qtd_saques_diario})")
        elif valor_saque > saldo:
            print(f"Saque no valor de R$ {valor_saque:.2f} indisponível, seu saldo atual é de R$ {saldo:.2f}")
        else:
            print(f"Valor inválido, o valor do saque deve ser positivo e no valor de até R$ {limite_saque:.2f} por saque")
    except ValueError:
        print("Opção inválida.")

def extrato():
    if not transacoes_extrato:
        print("Não há transações para demonstrar.")
    else:
        for transacao in transacoes_extrato:
            print(transacao)

while opcao != 0:
    try:
        opcao = int(input("""
Desafio DIO Sistema Bancário
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Sair

Escolha a opção desejada: """))

        if opcao == 1:
            depositar()
        elif opcao == 2:
            sacar()     
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print("Saindo do sistema!")
            break
        else:
            print("Digite uma opção válida")
    except ValueError:
        print("Opção inválida.")
