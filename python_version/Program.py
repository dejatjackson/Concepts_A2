from Block import Block

class Program(Block):
    def __init__(self, blk):
        if blk is None:
            raise TypeError("null block argument")
        self.blk = blk

    def execute(self):
        self.blk.process()