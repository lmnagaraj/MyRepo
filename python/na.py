class Naga:
 def __init__(self, name, age):
   self.name = name
   self.age = age

 def display(self):
   print(self.name)

class Mano(Naga):
 def __init__(self, sex):
   self.sex = sex

 def display(self):
  print("adkghja %s" % self.name)

vi = Mano("male")
print(vi.sex)

vi.name = "nagarajan"
vi.age = 10
vi.kdaf = 13
