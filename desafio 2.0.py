import textwrap

def depositar(saldo, valor, transacoes_extrato, /):
    try: 
        if valor > 0:    
            saldo += valor
            transacoes_extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f'=== Você depositou R$ {valor:.2f}, seu saldo atual é de R$ {saldo:.2f} ===')
        else: 
            print("@@@ Digite um valor válido @@@")
    except ValueError:
        print("@@@ Digite um valor válido @@@")
    return saldo, transacoes_extrato

def sacar(saldo, transacoes_extrato, limite_saque, qtd_saques_diario):
    try:
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        
        saldo_indisponivel = valor_saque > saldo
        limite_saque_diario_atingido = qtd_saques_diario == 0 
        limite_valor_saque_atingido = valor_saque > limite_saque

        if saldo_indisponivel:
            print("Saldo insuficiente.")
        elif limite_saque_diario_atingido:
            print("Limite de saques diários atingido.")
        elif limite_valor_saque_atingido:
            print(f"O valor de saque não pode exceder R$ {limite_saque:.2f}.")
        elif valor_saque > 0:
            saldo -= valor_saque
            transacoes_extrato.append(f"Saque: R$ {valor_saque:.2f}")
            qtd_saques_diario -= 1
            print(f'Você sacou R$ {valor_saque:.2f}, seu saldo atual é de R$ {saldo:.2f}')
        else:
            print("@@@ Digite um valor válido @@@")
    except ValueError:
        print("@@@ Digite um valor válido @@@")
    
    return saldo, transacoes_extrato, qtd_saques_diario

def extrato(saldo, transacoes_extrato):
    if not transacoes_extrato:
        print("Não há transações para exibir.")
    else:
        print("Extrato de transações:\n")
        for transacao in transacoes_extrato:
            print(transacao)
        print(f"\nSaldo atual: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def menu():
    menu =("""
        Desafio DIO Sistema Bancário
        
        ***************MENU***************
        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [4] - Criar usuário
        [5] - Criar conta
        [6] - Listar contas
        [7] - Sair

        **********************************
        Escolha a opção desejada: """)
    return input(textwrap.dedent(menu))

def main():
    AGENCIA = "0001"

    LIMITE_SAQUE = 500
    QTD_SAQUES_DIARIO = 3
    saldo = 0
    transacoes_extrato = []
    contas = [] 
    usuarios = []

    while True:
        opcao = int(menu()) 
        
        try:
            if opcao == 1:
                valor = float(input("Digite o valor que deseja depositar: "))

                saldo, transacoes_extrato = depositar(
                    saldo,
                    valor,
                    transacoes_extrato)
                
            elif opcao == 2:
                saldo, transacoes_extrato, QTD_SAQUES_DIARIO = sacar(
                    saldo=saldo,
                    transacoes_extrato=transacoes_extrato,
                    limite_saque=LIMITE_SAQUE,
                    qtd_saques_diario=QTD_SAQUES_DIARIO)
                
            elif opcao == 3:
                extrato(saldo, transacoes_extrato)

            elif opcao == 4:
                criar_usuario(usuarios)

            elif opcao == 5:
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                
                if conta:
                    contas.append(conta)

            elif opcao == 6:
                listar_contas(contas) 

            elif opcao == 7:
                print("\n======== Saindo do sistema =========\n")
                break

            else:
                print("\nDigite uma opção válida")

        except ValueError:
            print("Opção inválida.")

main()
