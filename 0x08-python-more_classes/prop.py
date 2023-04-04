class Geeks:
    def __init__(self):
        self._age = 0

    # using property decorator for getter fxn
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter fxn called
    @age.setter
    def age(self, a):
        if(a < 18):
            raise ValueError("Sorry you are underage, go home")
        print("setter method called")
        self._age = a

mark = Geeks()

mark.age = 19


print(mark.age)

