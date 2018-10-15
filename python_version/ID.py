import Arithmetic_expression
import Memory

class ID():
    def __init__(self, id):
        self.id = id

    def evaluate(self):
        return Memory.Memory.fetch(self.id) #TODO

    def getChar(self):
        return self.id
