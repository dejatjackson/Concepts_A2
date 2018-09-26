import Statement
import Arithmetic_expression


class Assignment_statement():
    def __init__(self, var, a_express):
        if a_express == None:
            raise TypeError("null Expression");
        if var == None:
            raise TypeError("null Id");
        self.var = var
        self.a_express = a_express

    def execute(self):
        Memory.store(self.var.getChar(), self.a_express.evaluate())