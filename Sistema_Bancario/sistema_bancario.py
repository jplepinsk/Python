import os
#3 saques diarios 500 por saque, ver limite

extrato = []
saldo = 0
limite_quant_saques = 3
contador_saques_diarios = 0
limite_por_saque = 500

def deposito():
    global saldo
    os.system('cls')
    print("- "*20)
    print("*** Depósito ***")
    print("- "*20)
    try:
        deposito = float(input("Qual o valor que deseja depositar R$: "))
        if deposito <= 0:
            print("Erro! Valor não pode ser igual ou menor a ZERO!")
        else:
            saldo += deposito
            print("OK! Valor depositado com sucesso!")
            print(f"*** Saldo atual: R$ {saldo:.2f} ***")
            extrato.append(f"DEPÓSITO - R$ {deposito:.2f}")
    except:
        print("Valor inválido!")

def saque():
    global saldo, limite_por_saque, limite_quant_saques, contador_saques_diarios
    os.system('cls')
    print("- "*20)
    print("*** Saque ***")
    print("- "*20)
    try:
        saque = float(input("Qual o valor que deseja sacar R$: "))
        if saque <= 0:
            print("Erro! Valor não pode ser igual ou menor a ZERO!")
        elif saque > limite_por_saque:
            print("Erro! Valor está acima do permitido por saque!")
        elif contador_saques_diarios >= limite_quant_saques:
            print("Erro! Você ultrapassou o limite de saques diários!")
        else:
            saldo -= saque
            print("OK! Valor sacado com sucesso!")
            print(f"*** Saldo atual: R$ {saldo:.2f} ***")
            contador_saques_diarios += 1
            extrato.append(f"SAQUE - R$ {saque:.2f}")
    except:
        print("Valor inválido!")

def consultar_saldo():
    global saldo
    os.system('cls')
    print("- "*20)
    print("*** C0nsulta de Saldo ***\n")
    print("- "*20)
    print(f"*** SALDO ATUAL: R$ {saldo:.2f}")
    print("- "*20)
    
def imprimir_extrato():
    global saldo
    os.system('cls')
    print("- "*20)
    print("*** Impressão de extrato ***")
    print("- "*20)
    if not extrato:
        print("Não há movimentações na conta!")
    else:
        for item in extrato:
            print(f"- {item}")
        else:
            print("*** Fim da impressão *** ")
            print(f"*** SALDO ATUAL : R$ {saldo:.2f}")



while True:
    os.system('cls')
    print("- "*20)
    print("*** Sistema bancário ***")
    print("- "*20)
    print("      Opções     ")
    print("[1] DEPOSITAR")
    print("[2] SACAR")
    print("[3] SALDO")
    print("[4] EXTRATO")
    print("[5] SAIR")
    opcao = input("Qual a sua opção?: ")
    
    if opcao == '1':
        deposito()
    elif opcao == '2':
        saque()
    elif opcao == '3':
        consultar_saldo()
    elif opcao == '4':
        imprimir_extrato()
    elif opcao == '5':
        print("Encerrando o sistema ...")
        break
    else:
        print("Opção inválida!")

    
    os.system('pause')
