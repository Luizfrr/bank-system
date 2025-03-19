import transactions

saldo_conta:float = 0.0
quant_saques:int = 0
valor:float = 0.0
historico_deposito = []
historico_saque = []
escolha_menu = ""

while True:
    escolha_menu = input("""\n======= MENU DE OPÇÕES =======
    1 - Consultar extrato
    2 - Depositar
    3 - Sacar
    4 - Sair\n -> """)

    if(escolha_menu == "1"):
        transactions.extract(historico_deposito, historico_saque)

    elif(escolha_menu == "2"):
        valor = float(input("\nDigite o valor: "))
        saldo_conta, historico_deposito = transactions.deposit(valor, saldo_conta, historico_deposito)

    elif(escolha_menu == "3"):
        if(quant_saques <=3):
            valor = float(input("\nDigite o valor: "))
            quant_saques += 1
        else:
            print("\nLimite de saque diários atingido")
        saldo_conta, historico_saque = transactions.sake(valor, saldo_conta, historico_saque)

    elif(escolha_menu == "4"):
        break

    else:
        print("\nEscolha uma opção válida")

    print(f"\nSaldo atual: {saldo_conta}")