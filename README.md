# bank-system

# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples em Python, permitindo que o usuário realize operações como:

- Consultar extrato
- Depositar valores
- Sacar dinheiro (com limite de saques diários)
- Sair do sistema

## Estrutura do Projeto

O projeto possui os seguintes arquivos:

```
BANK-SYSTEM/
│── main.py           # Arquivo principal que executa o sistema
│── transactions.py   # Módulo com as funções de transação bancária
│── README.md         # Documentação do projeto
```
## Funcionalidades

### 1. Consultar Extrato
O usuário pode consultar o histórico de transações (depósitos e saques):
```
======= MENU DE OPÇÕES =======
1 - Consultar extrato
2 - Depositar
3 - Sacar
4 - Sair
 -> 1
DEPÓSITOS:
1º R$100.00
SAQUES:
1º R$-50.00
```

### 2. Depositar
O usuário pode inserir um valor positivo para adicionar ao saldo:
```
Digite o valor: R$200
Valor depositado: R$ 200.00
Saldo atual: R$200.00
```

### 3. Sacar
- O saque é limitado a R$500 por transação.
- O usuário pode sacar no máximo 3 vezes por dia.
- O saldo precisa ser suficiente para a operação.
```
Digite o valor: R$50
Valor sacado: R$ 50.00
Saldo atual: R$150.00
```

Caso o saldo seja insuficiente:
```
Saldo insuficiente
```

Se o limite de saques for atingido:
```
Limite de saques diários atingido
```

### 4. Sair
O usuário pode sair do sistema digitando `4` no menu.