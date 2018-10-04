import Relative_op
import Arithmetic_expression

class Boolean_expression(Relative_op):

    def __init__(self,op, expr1, expr2 ):
        if op is None:
            raise TypeError("Relational operator argument cannot be null!")
        if expr1 is None or expr2 is None:
            raise TypeError("Arithmetic expression argument cannot be null!")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def eval(self):
        result = False
        if self.op == self.eq_operator:
            result = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.op == self.ne_operator:
            result = self.expr1.evaluate() != self.expr2.evaluate()
        elif self.op == self.lt_operator:
            result = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == self.le_operator:
            result = self.expr1.evaluate() <= self.expr2.evaluate()
        elif self.op == self.gt_operator:
            result = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == self.ge_operator:
            result = self.expr1.evaluate() >= self.expr2.evaluate()
        return result