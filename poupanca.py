from conta import Conta

class Poupanca(Conta):

    def __init__(self, id_account, balance, yield_rate):
        super().__init__(id_account, balance)
        self._yield_rate = yield_rate


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
        
    def __convert_to_mounthly_rate(self) -> float:
        return (((1 + (self.yield_rate/100)) ** (1/12)) - 1)
        
        
    def __process_rate_compound_method(self, time_measure: str) -> float:
        
        match time_measure:
            case 's':
                return self.__convert_to_mounthly_rate/(30*24*60*60)
            case 'm':
                return self.__convert_to_mounthly_rate/(30*24*60)
            case 'h':
                return self.__convert_to_mounthly_rate/(30*24)
            case 'D':
                return self.__convert_to_mounthly_rate/30
            case 'M':
                return self.__convert_to_mounthly_rate
            case 'A':
                return self.yield_rate/100
            case _:
                return -1.0



    # O calculo do rendimento foi feito utilizando juros compostos
    def calculate_income_compound_method(self, time: str) -> float:
        
        if(len(time) > 1):
            time_measure = time[-1]
            time = int(time[:-1])
        
            if(time > 0):
                processed_rate = self.__process_rate_compound_method(time_measure)
            else:
                raise TypeError("Time measure is not correctly typed")

            if(processed_rate >= 0):
                income = self.balance * pow(1 + processed_rate, time)
                return income
            else:
                raise Exception("Time measure is not valid")
        else:
            raise TypeError("Time measure is not correctly typed")


