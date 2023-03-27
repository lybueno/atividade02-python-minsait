from conta import Conta

class Poupanca(Conta):

    def __init__(self, id_account: int, balance: float, yield_rate: float):
        super().__init__(id_account, balance)
        self._yield_rate: float = yield_rate


    @property
    def yield_rate(self):
        return self._yield_rate
    

    @yield_rate.setter
    def yield_rate(self, new_rate):
        if(self._is_valid(new_rate)):
            self._yield_rate = new_rate


    def deposit(self, amount: float):
        if(self._is_valid(amount)):
            self.balance += amount
        else:
            raise ValueError("Amount cannot be negative.")
        

    def withdraw(self, amount: float):        
        if(not(self._is_valid(amount))):
            raise ValueError("Amount cannot be negative")
        if(amount <= self.balance):
            self.balance -= amount
        else:
            raise Exception("Amount exceeds your limit account.")
        

    # O calculo do rendimento foi feito utilizando juros compostos
    def calculate_income_compound_method(self, processed_rate: float, time: int) -> float:
        if(processed_rate >= 0):
            income = self.balance * pow(1 + processed_rate, time)
            return income
        else:
            raise Exception("Time measure is not valid")

# Os metodos de calculo de taxa equivalente e tratamento do tempo foram retirados para que a classe nao
# possua responsabilidades que nao dizem respeito a sua regra de negócio (a Poupanca deve calcular o 
# rendimento, apenas). A responsabilidade do calculo da taxa equivalente agora e da classe RateFormatter 
# e, do tratamento da quantidade de tempo da classe TimeFormatter

