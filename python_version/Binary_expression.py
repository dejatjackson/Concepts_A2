from Arithmetic_expression import Arithmetic_expression
from Arithmetic_op import Arithmetic_op
from Relative_op import Relative_op
import enum

class Binary_expression(Arithmetic_expression):


    def __init__(self, op, expr1, expr2):
        if op is None:
            raise TypeError("null arithmetic operator argument")
        if expr1 is None or expr2 is None:
            raise TypeError("null expression argument")
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op

    def evaluate(self):

        v = 0
        if self.op == Arithmetic_op.add_operator:
            v = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == Arithmetic_op.mul_operator:
            v = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == Arithmetic_op.div_operator:
            v = self.expr1.evaluate() / self.expr2.evaluate()
        elif self.op == Arithmetic_op.sub_operator:
            v = self.expr1.evaluate() - self.expr2.evaluate()
        return v