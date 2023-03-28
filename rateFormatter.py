
class RateFormatter():

    def __init__(self, rate: float):
        self._rate: float = rate


    @property
    def rate(self):
        return self._rate
    
    
    @rate.setter
    def rate(self, new_rate: str):
        self._rate = new_rate


    def __convert_to_mounthly_rate(self) -> float:
        return (((1 + (self.rate/100)) ** (1/12)) - 1)
    

    def process_rate_compound_method(self, time: str) -> float:

        if(len(time) > 1):
            time_measure = time[-1]
            time = int(time[:-1])
        
            if(time > 0):
    
                match time_measure:
                    case 's':
                        return self.__convert_to_mounthly_rate()/(30*24*60*60)
                    case 'm':
                        return self.__convert_to_mounthly_rate()/(30*24*60)
                    case 'h':
                        return self.__convert_to_mounthly_rate()/(30*24)
                    case 'D':
                        return self.__convert_to_mounthly_rate()/30
                    case 'M':
                        return self.__convert_to_mounthly_rate()
                    case 'A':
                        return self.rate/100
                    case _:
                        return -1.0
            else:
                raise TypeError("Time measure is not correctly typed")
            
        else:
            raise TypeError("Time measure is not correctly typed")