def balaji(naga):
	def wrapper(*args):
		print("Function modified")
		return naga(*args)
	return wrapper

@balaji
def naga(x, y):
	print( x + y)

naga(10, 20)
