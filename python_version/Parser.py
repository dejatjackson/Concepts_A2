
#TODO - complete all methods below
import ParserException
import token

class Parser():
    def _init_(self, filename):
        self.filename = filename

    def parse(self):

    def getBlock(self):

    def getStatement(self):

    def getPrintStatement(self):

    def getWhileStatement(self):

    def getForStatement(self):

    def getIfStament(self):

    def isValidStartOfStatement(self):

    def getArithmeticExpression(self):

    def getBinaryExpression(self):


    def getArithmeticOperator(self):

    def getLiteralInteger(self):

    def getId(self):

    def getBooleanExpression(self):


    def getRelationalOperator(self):

    def match(self):

    def getLookaheadToken(self):

    def getNextToken(self): #TODO - I think this is wrong, just saying
            tok = null
            try:
                tok = lex.getNextToken()
                raise ParserException
            except:
                print("no more tokens")
            return tok

    