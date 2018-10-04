import Arithmetic_expressions
import Memory

class ID(Memory):
    def __init__(self, id):
        self.id = id

    def evaluate(self):

        return self.fetch(self.id)

    def getChar(self):
        return self.id
