from contaCorrente import ContaCorrente
from poupanca import Poupanca
from menu_periodo import MenuPeriodo
from rateFormatter import RateFormatter
from timeFormatter import TimeFormatter

##### testando metodos da conta corrente #######
contaCorrente = ContaCorrente(account_id=1, balance=1000.0, account_limit=100.0)

# verificando se é lançado erro ao depositar valor negativo
#contaCorrente.deposit(-100.0)

# verificando deposito de valor válido
contaCorrente.deposit(100.0)
print(contaCorrente.balance)

# verificando se é lançado erro ao sacar valor negativo
#contaCorrente.withdraw(-100.0)

# verificando se é lançado erro ao sacar valor maior que o valor em conta
#contaCorrente.withdraw(1550.0)

# verificando saque de valor válido
contaCorrente.withdraw(500.0)
print(contaCorrente.balance)


#### Testando metodos da poupança ######
poupanca = Poupanca(id_account=2, balance=1000.0, yield_rate=10)

## exibir opções
menu = MenuPeriodo()
periodo_para_calcular_rendimento = menu.exibir()

formatador_taxa = RateFormatter(rate=poupanca.yield_rate)
taxa = formatador_taxa.process_rate_compound_method(periodo_para_calcular_rendimento)

formatador_tempo = TimeFormatter(periodo_para_calcular_rendimento)
tempo = formatador_tempo.format_time()

## testando metodo de rendimento
print(f"{round(poupanca.calculate_income_compound_method(taxa, tempo), 2)}")

# verificando se é lançado erro ao depositar valor negativo
#poupanca.deposit(-100.0)

# verificando deposito de valor válido
poupanca.deposit(500.0)
print(poupanca.balance)

# verificando se é lançado erro ao sacar valor negativo
#poupanca.withdraw(-100.0)

# verificando se é lançado erro ao sacar valor maior que o valor em conta
#poupanca.withdraw(1550.0)

# verificando saque de valor válido
poupanca.withdraw(800.0)
print(poupanca.balance)

