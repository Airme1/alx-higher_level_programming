class Time:
    def __init__(self, hour= 0, minute= 0):
        self._hour = hour
        self._minute = minute

    def get_hour(self):
        return self._hour

    def set_hour(self, hrs):
        self._hour = hrs

    def get_minute(self):
        return self._minute

    def set_minute(self, min):
        self._minute = min


clock = Time()

clock.set_minute(15)
clock.set_hour(1)

print(clock.get_hour())
