class Square():
    """A class to find area of a square with a private instance attribute"""

    def __init__(self, size=0):
        try:
            type(size) == type(int)
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError:
                print("size must be >=0")
        self.__size = size

    def area(self):
        return self.__size * self.__size