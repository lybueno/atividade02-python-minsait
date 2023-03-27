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
        if(self.is_valid(new_rate)):
            self._yield_rate = new_rate


    def deposit(self, amount: float):
        if(self.is_valid(amount)):
            self.balance += amount
        else:
            raise ValueError("Amount cannot be negative.")
        

    def withdraw(self, amount: float):        
        if(not(self.is_valid(amount))):
            raise ValueError("Amount cannot be negative")
        if(amount <= self.balance):
            self.balance -= amount
        else:
            raise Exception("Amount exceeds your limit account.")
        
        
    def process_rate_compound_method(self, time_measure: str) -> float:
        mounth_converted = (((1 + (self.yield_rate/100)) ** (1/12)) - 1)

        match time_measure:
            case 's':
                return mounth_converted/(30*24*60*60)
            case 'm':
                return mounth_converted/(30*24*60)
            case 'h':
                return mounth_converted/(30*24)
            case 'D':
                return mounth_converted/30
            case 'M':
                return mounth_converted
            case 'A':
                return self.yield_rate/100
            case _:
                return -1.0


    def calculate_income_compound_method(self, time: str) -> float:
        time_measure = time[-1]
        time = int(time[:-1])
        
        processed_rate = self.process_rate_compound_method(time_measure)

        if(processed_rate > 0):
            income = self.balance * pow(1 + processed_rate, time)
            return income
        else:
            raise Exception("Time measure is not valid")


