import Block

class Program():
    def __init__(self, blk):
        if blk == None:
            raise TypeError("null block argument")
        self.blk = blk

    def execute(self):
        self.blk.process()