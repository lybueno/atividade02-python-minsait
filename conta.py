from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, account_id: int, balance: float):
        self.__account_id: int = account_id
        self._balance: float = balance


    def _is_valid(self, value: float) -> bool:
        return value >= 0.0
    

    @property
    def account_id(self):
        return self.__account_id
    

    @property
    def balance(self):
        return self._balance
    

    @balance.setter
    def balance(self, new_balance: float):
        if(self._is_valid(new_balance)):
            self._balance = new_balance
        else:
            raise ValueError("New balance cannot be negative")


    @abstractmethod
    def deposit(self, amount: float):
        pass


    @abstractmethod
    def withdraw(self, amount: float):
        pass

"""
    A Classe Conta é abstrata, pois para a regra de negócio não faz sentido instanciar uma conta e sim conta corrente e poupança
    Não foi implementado o setter do atributo account_id pois não é recomendado deixar código cliente alterar o ID de um objeto
"""