
import Arithmetic_expression

class Literal_integer(Arithmetic_expression):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value