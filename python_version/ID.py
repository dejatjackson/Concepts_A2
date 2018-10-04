import Arithmetic_expressions

class ID:
    def __init__(self, id):
        self.id = id

    def evaluate(self):

        return Memory.fetch(self.id) #TODO: No lcue on how to fix this yet

    def getChar(self):
        return self.id
