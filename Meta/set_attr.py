class Naga():
        __slots__ = ["name", "age"]
        def __init__(self, name, age):
                for x in self.__slots__:
                        setattr(self, x, x)
