import Statement
import Arithmetic_expression
import Memory
import ID


class Assignment_statement(Statement,Memory):
    def __init__(self, var, a_express):
        if a_express is None:
            raise TypeError("null Expression")
        if var is None:
            raise TypeError("null Id")
        self.var = var
        self.a_express = a_express

    def execute(self):
        self.store(self.var.getChar(), self.a_express.evaluate())