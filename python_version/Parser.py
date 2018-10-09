
#TODO - complete all methods below
import ParserException
import token
import Arithmetic_expression
import PrintStatement

class Parser():
    def _init_(self, filename):
        self.filename = filename

    def parse(self):

    def getBlock(self): #TODO - I think this is wrong, just saying

        #TODO how to i do the throws ParserException thing

        blk = Block() #TODO
        tok = getLookaheadToken() #TODO
        while(isValidStartOfStatement(tok)):
            Statement.stmt = getStatement() #TODO
            blk.add(stmt)
            tok = getLookaheadToken()
        return blk

    def getStatement(self):
        #TODO how to i do the throws ParserException thing
        stmt #TODO
        tok = getLookaheadToken() #TODO
        if tok.getTokType() == tokentype.if_tok:
            stmt = getIfStatement()
        else if tok.getTokType == tokentype.while_tok:
            stmt = getWhileStatement()
        else if tok.getTokType ==


    def getPrintStatement(self):
        tok = self.getNextToken()
        self.match(tok, tokentype) #TODO
        tok = self.getNextToken()
        self.match(tok, tokentype) #TODO
        expr = Arithmetic_expression.Arithmetic_expression()
        tok = self.getNextToken
        self.match(tok, tokentype) #TODO
        return PrintStatement.PrintStatement(expr)


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

    