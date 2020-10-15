class Naga():
	__balaji = "private"
	def __init__(self, name):
		self.name = name
		self.__private_method()
	@classmethod
	def test_mymthod(cls):
		print(" i am calling from {} " .format(cls))
	@staticmethod
	def test_mystatic():
		print("i am from Static method")
	def print_private(self):
		print(self.__balaji)
	def __private_method(self):
		print("hi i am called from private method")
	def _protected_method(self):
		print("hi i am called from protected")
	def call_my_private(self):
		self.__private_method()

