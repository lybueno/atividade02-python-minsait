
class TimeFormatter():

    def __init__(self, time: str):
        self._time: str = time

    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, new_time):
        self.time = new_time

    def format_time(self) -> int:
        if len(self.time) > 1:
            return int(self.time[:-1])
        else:
            return 0