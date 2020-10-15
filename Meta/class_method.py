class Naga():
        instances = 0
        def __init__(self):
                self.add_instances()

        @classmethod
        def add_instances(cls):
                cls.instances += 1

        def tota_instances(self):
                print(self.instances)

class Raj(Naga):
        instances = 0
        def __init__(self):
                super().__init__()
