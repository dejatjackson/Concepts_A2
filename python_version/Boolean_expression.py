import Relative_op
import Arithmetic_expression

class Boolean_expression():

    def __init__(self,op, expr1, expr2 ):
        if op == None:
            raise TypeError("Relational operator argument cannot be null!")
        if expr1 == None or expr2 == None:
            raise TypeError("Arithmetic expression argument cannot be null!")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def eval(self):
        result = self.false
        if self.op == eq_operator:
            result = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.op == ne_operator:
            result = self.expr1.evaluate() != self.expr2.evaluate()
        elif self.op == lt_operator:
            result = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == le_operator:
            result = self.expr1.evaluate() <= self.expr2.evaluate()
        elif self.op == gt_operator:
            result = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == ge_operator:
            result = self.expr1.evaluate() >= self.expr2.evaluate()
        return self.result