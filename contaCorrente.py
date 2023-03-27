from conta import Conta

class ContaCorrente(Conta):

    def __init__(self, account_id: int, balance: float, account_limit: float):
        super().__init__(account_id, balance)
        self._account_limit: float = account_limit


    @property
    def account_limit(self):
        return self._account_limit
    

    @account_limit.setter
    def account_limit(self, new_limit):
        if(self._is_valid(new_limit)):
            self._account_limit = new_limit


    def deposit(self, amount: float):
        if(self._is_valid(amount)):
            self.balance = self.balance + amount
        else:
            raise ValueError("Amount cannot be negative")


    def withdraw(self, amount: float):
        total = self.account_limit + self.balance

        if(not(self._is_valid(amount))):
            raise ValueError("Amount cannot be negative")
        if(amount <= total):
            self.balance -= amount
        else:
            raise Exception("Amount exceeds your limit account.")