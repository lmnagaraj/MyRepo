class Naga():
	__slots__ = [ 'x', 'y', 'z' ]
	def __init__(self):
		for x in self.__slots__:
			setattr(self, x, x)
