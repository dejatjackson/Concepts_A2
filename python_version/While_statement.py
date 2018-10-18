from Statement import Statement
from Boolean_expression import Boolean_expression
from Block import Block

class While_statement(Statement):

    def __init__(self, b_expr, blk):

        if b_expr is None:
            raise TypeError("null boolean expression")
        if blk is None:
            raise TypeError("null block")

        self.b_expr = b_expr
        self.blk = blk

    def execute(self):
        while(self.b_expr.eval()):
            self.blk.process()
