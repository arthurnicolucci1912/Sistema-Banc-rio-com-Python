class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_POR_SAQUE = 500.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_realizados >= self.LIMITE_SAQUES:
            print("Limite diário de saques atingido (3 saques por dia).")
            return

        if valor > self.LIMITE_POR_SAQUE:
            print(f"Limite máximo por saque é R$ {self.LIMITE_POR_SAQUE:.2f}.")
            return

        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return

        self.saldo -= valor
        self.extrato.append(f"Saque: -R$ {valor:.2f}")
        self.saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def ver_extrato(self):
        print("\n============= EXTRATO =============")
        if not self.extrato:
            print("Nenhuma operação realizada.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("===================================")

# Exemplo de uso:
banco = SistemaBancario()

# Menu interativo
while True:
    print("\n[1] Depositar | [2] Sacar | [3] Extrato | [0] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: R$ "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = float(input("Valor do saque: R$ "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.ver_extrato()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")