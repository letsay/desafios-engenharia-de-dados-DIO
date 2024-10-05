#criar sistema bancário p
saldo = 0
extrato = ""
numero_de_saques = 0
valor_limite = 500
deposito = 0
LIMITE_SAQUES = 3
extrato_mensagem = "EXTRATO"
espaco = ""

menu = """
 ------------------------
|  Qual opção deseja?    |
|  [1] Visualizar extrato|
|  [2] Realizar saque    |
|  [3] Realizar depósito |
|  [4] Sair              |
 ------------------------
"""

def visualizar_extrato():
    print(extrato_mensagem.center(40, "="))
    print ("Não foram relizadas movimentações" if not extrato else extrato)
    print (f"\nSaldo:    R$ {saldo:.2f}")
    print (espaco.center(40, "="))

def realizar_saque():
    global extrato, saldo, numero_de_saques
    saque = float(input("Valor que deseja sacar:\n"))

    excedeu_saldo = saque > saldo
    excedeu_limite = saque > valor_limite
    excedeu_saques = numero_de_saques >= LIMITE_SAQUES

    if excedeu_saldo or excedeu_limite:
        print(f"Valor de saque inválido!")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif saque > 0:
            saldo -= saque
            extrato += f"Saque:    R$:{saque:.2f}\n"
            numero_de_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido!")

def realizar_deposito():
    global extrato, saldo
    deposito = float(input("Qual o valor de depósito?\n"))
    if deposito < 0:
        print("Valor inválido.")
            
    else:
        print(f"Depósito: R${deposito:.2f}\n")
        saldo += deposito 
        extrato += f"Depósito: R$:{deposito:.2f}\n"

while True:
    print(menu)
    opcao = int(input ("==> "))
    if opcao == 1:
        visualizar_extrato()
    elif opcao == 2:
        realizar_saque()
    elif opcao == 3:
        realizar_deposito()
    elif opcao == 4:
        break
    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")
