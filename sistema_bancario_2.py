#criar sistema bancário p
from datetime import date, datetime, time

saldo = 0
extrato = ""
numero_de_saques = 0
valor_limite = 500
deposito = 0
AGENCIA = "0001"
LIMITE_SAQUES = 3
extrato_mensagem = "EXTRATO"
espaco = ""
usuarios = []
contas = []
numero_conta = 1
ano = 1
mes = 1
dia = 1
mascara_ptbr = "%d/%m/%Y"

menu = """
 --------------------------
|  Qual opção deseja?      |
|  [1] Visualizar extrato  |
|  [2] Realizar saque      |
|  [3] Realizar depósito   |
|  [4] Novo usuário        |
|  [5] Nova conta corrente |
|  [6] Listar contas       |
|  [7] Sair                |
 --------------------------
"""
def visualizar_extrato(saldo, /, *, extrato):
    print(extrato_mensagem.center(40, "="))
    print("Não foram relizadas movimentações" if not extrato else extrato)
    print (f"\nSaldo:\t\tR${saldo:.2f}")
    print (espaco.center(40, "="))

def realizar_saque():
    global extrato, saldo, numero_de_saques
    saque = float(input("Valor que deseja sacar:\n"))
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > valor_limite
    excedeu_saques = numero_de_saques >= LIMITE_SAQUES
    if excedeu_saldo or excedeu_limite:
        print("Valor de saque inválido!")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif saque > 0:
            saldo -= saque
            extrato += f"Saque:\t\tR${saque:.2f}\n"
            numero_de_saques += 1
            print(f"Saque de R${saque:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
                
deposito_funcoes = {
    'print_deposito': lambda deposito: print(f"Depósito de R${deposito:.2f} realizado com sucesso!\n") if deposito > 0 else print("Valor inválido"),
    'pega_deposito':lambda deposito: deposito,
    'atualiza_saldo':lambda deposito: saldo + deposito,
    'add_extrato':lambda deposito: f"Depósito:\tR${deposito:.2f}\n"}

def filtra_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def data_func():
    ano = int(input("insira o ano de nascimento: "))
    mes = int(input("insira o mês de nascimento: "))
    dia = int(input("insira o dia do seu nascimento: "))
    global data_nascimento 
    data_nascimento = date(ano, mes, dia).strftime(mascara_ptbr)

def endereco_func():
    logradouro = input("Logradouro: ")
    nro = int(input("Número: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla_estado = input("Sigla do estado: ")
    global endereco
    endereco = f"{logradouro},  {nro} - {bairro} - {cidade}/{sigla_estado}"
    
def cria_usuario(usuarios):
    cpf = input("Insira seu CPF (somente números): ")
    usuario = filtra_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com esse CPF")
        return
    while True:
        p_nome = input("Nome: ")
        if all(caractere.isalpha() for caractere in p_nome):
            break
        else:
            print('Digite somente o primeiro nome.')
    while True:
        sobrenome = input("Sobrenome: ")
        if all(caractere.isalpha() for caractere in sobrenome):
            break
        else:
            print('Digite somente o sobrenome.')
    nome = p_nome + " " + sobrenome
    data_func() 
    endereco_func()
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("Usuário criado com sucesso!")

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtra_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {'agencia': AGENCIA, 'numero_conta': numero_conta, 'usuario': usuario}
    print("Usuário não encontrado, fluxo de criação de conta encerrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

while True:
    print(menu)
    opcao = int(input ("==> "))
    if opcao == 1:
        visualizar_extrato(saldo, extrato = extrato)
    elif opcao == 2:
        realizar_saque()
    elif opcao == 3:
        deposito = float(input("Qual o valor de depósito?\n"))
        deposito_funcoes['print_deposito'](deposito) 
        if deposito > 0:
            saldo = deposito_funcoes['atualiza_saldo'](deposito)  
            extrato += deposito_funcoes['add_extrato'](deposito)
    elif opcao == 4:
        cria_usuario(usuarios)
    elif opcao == 5:
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta: 
            contas.append(conta)
            numero_conta += 1
    elif opcao == 6:
        listar_contas(contas)
    elif opcao == 7:
        break
    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")
