import Arithmetic_expression
import Arithmetic_op
import Relative_op
import enum

class Binary_expression(Arithmetic_expression, Arithmetic_op, Relative_op):


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
        if self.op == self.add_operator:
            v = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == self.mul_operator:
            v = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == self.div_operator:
            v = self.expr1.evaluate() / self.expr2.evaluate()
        elif self.op == self.sub_operator:
            v = self.expr1.evaluate() - self.expr2.evaluate()
        return v