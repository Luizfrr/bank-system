def deposit(value:float, balance:float, deposits_history = None):
    if deposits_history is None:    
        deposits_history = []

    new_Value = value

    if(new_Value > 0):
        balance += new_Value
        deposits_history.append(new_Value)
        print(f"\nValor depositado: R${new_Value: .2f}")

    else:
        print("\nO valor inserido não pode ser depositado na conta")

    return balance, deposits_history

def sake(value:float, balance:float, sake_history = None):
    if sake_history is None:    
        sake_history = []

    new_Value = value

    if(new_Value > balance):
        print("\nSaldo insuficente")

    elif(new_Value < 0):
        print("\nO valor inserido não pode ser sacado da conta")

    elif(new_Value <= 500):
        balance-= new_Value
        sake_history.append(-new_Value)
        print(f"\nValor sacado: R${new_Value: .2f}")

    else:
        print("\nValor inválido")

    return balance, sake_history

        

def extract(deposits_history = None, sake_history = None):
    print("DEPÓSITOS: ")
    for i in range(len(deposits_history)):
        print(f"{i + 1}º R${deposits_history[i]:.2f}")

    print("SAQUES: ")
    for i in range(len(sake_history)):
        print(f"{i + 1}º R${sake_history[i]:.2f}")
