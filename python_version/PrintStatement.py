class PrintStatement:

    def __init__(self, expr):
        if expr is None:
            raise ValueError("Expression cannot be empty")
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())