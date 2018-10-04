import Statement
import Block

class if_statement(Statement,Block):
    def __init__(self, b_expr, blk1, blk2):
        self.b_expr = b_expr
        self.blk1 = blk1
        self.blk2 = blk2

    def execute(self):
        if self.b_expr.eval():
            self.blk1.process()
        else:
            self.blk2.process()



