# Conta bancaria:

class ContaBancaria:
  def __init__(self, numero_conta, saldo = 0):
    self.numero_conta = numero_conta
    self.saldo = saldo
    self.transacoes = []

  def depositar(self, valor):
    self.saldo += valor
    self.transacoes.append(f"Deposito de {valor}")

def sacar(self, valor):
  if self.saldo >= valor:
    self.saldo -= valor
    self.transacoes.append(f"Saque de {valor}")
  else:
    print("Saldo insuficiente")

def consultar_saldo(self):
  print("Saldo:", self.saldo)

def registrar_transacao(self, tipo, valor):
  self.transacoes.append({"Tipo": tipo, "Valor": valor})


class ContaCorrente(ContaBancaria):
  def __init__(self, numero_conta, limite_cheque_especial = 0):
    super().__init__(numero_conta)
    self.limite_cheque_especial = limite_cheque_especial

  def sacar(self, valor):
    if self.saldo + self.limite_cheque_especial >= valor:
      self.saldo -= valor
      self.registrar_transacao("Emissaõ de Cheque", valor)
    else:
      print("Limite de cheque especial excedido.")

class ContaPoupanca(ContaBancaria):
  def calcular_juros_mensal(self, taxa_juros):
    juros = self.saldo * (taxa_juros / 100)
    self.saldo += juros
    self.registrar_transacao("Juros Mensais", juros)

class ContaInvestimento(ContaBancaria):
  def __init__(self, numero_conta):
    super().__init__(numero_conta)
    self.investimentos = []
    
  def realizar_investimento(self, produto, valor):

# Lógica para realizar o investimento

    self.registrar_transacao("Investimento", valor)


# ---- Calculadora de Tarifa: ----- #

class CalculadoraTarifas:
    @staticmethod
    def calcular_tarifa_base():
        return 5 # Exemplo: tarifa base de R$ 5 para todas as contas
    
@staticmethod
def calcular_tarifa_transacao(numero_transacoes):
        if numero_transacoes > 10:
            return (numero_transacoes - 10) * 1.5 # Exemplo: R$ 1,50 por transação adicional
        else:
            return 0
        
@staticmethod
def calcular_tarifa_saldo(saldo):
        if saldo < 1000:
            return 10 # Exemplo: tarifa de R$ 10 para saldos abaixo de R$ 1000
        else:
            return 0