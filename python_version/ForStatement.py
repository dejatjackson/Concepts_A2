class ForStatement:

    def __init__( self, bool, blk):

        if bool is None:
            raise ValueError("null boolean expression")
        elif blk is None:
            raise ValueError("null black")

        self.bool = bool
        self.blk = blk


    def execute(self):
        #while(bool.eval()):
            #blk.process()

        while True:
            self.blk.process()
            if self.bool.eval() != True:
                break
