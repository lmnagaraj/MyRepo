class Naga():
	total_instances = 0
	def __init__(self):
		self.add_instances()

	@classmethod
	def add_instances(cls):
		cls.total_instances += 1

	def print_total(self):
		print("The total instances are {} " .format(self.total_instances))

class Raj(Naga):
	total_instances = 0
	def __init__(self):
		super().__init__()

class lakshmi(Raj, Naga):
	pass
