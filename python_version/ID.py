<<<<<<< HEAD
from Arithmetic_expression import Arithmetic_expression

=======
import Arithmetic_expression
>>>>>>> 005bd2719ae4a7b48f8f72f3780a8328987a94b9
import Memory

class ID():
    def __init__(self, id):
        self.id = id

    def evaluate(self):
        return Memory.Memory.fetch(self.id) #TODO

    def getChar(self):
        return self.id
