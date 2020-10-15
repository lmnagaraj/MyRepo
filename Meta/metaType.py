class mytype(type):
    def __new__(cls, clsname, bases, clsdict):
        if len(bases) > 1:
            raise TypeError("No....")
        return super().__new__(cls, clsname, bases, clsdict)
