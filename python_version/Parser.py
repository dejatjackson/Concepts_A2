
#TODO - complete all methods below
import ParserException
import token
import Block
import Statement
import BooleanExpression
import ArthmeticExpression
import IfStatement


class Parser():
    def _init_(self, filename):
        self.filename = filename

    def parse(self):

    def getBlock(self):

        #TODO how to i do the throws ParserException thing

        blk = Block.Block() #TODO
        tok = self.getLookaheadToken()
        while(self.isValidStartOfStatement(tok)):
            stmt = self.getStatement() #TODO
            blk.add(stmt)
            tok = self.getLookaheadToken()
        return blk

    def getStatement(self):
        #TODO how to i do the throws ParserException thing
        tok = self.getLookaheadToken()
        if tok.getTokType() == tokentype.if_tok: #TODO
            stmt = self.getIfStatement()
        else if tok.getTokType == tokentype.while_tok: #TODO
            stmt = self.getWhileStatement()
        else if tok.getTokType == tokentype.print_tok:  #TODO
                stmt = self.getPrintStatement()
        else if tok.getTokType == tokentype.for_tok: #TODO
            stmt = self.getForStatement()
        else if tok.getTokType == tokentype.id: #TODO
            stmt = self.getAssignmentStatement()
        return stmt

    def AssignmentStatement(self):
        var = self.getID()
        tok = self.getNextToken()
        self.match(tok, tokentype.assignment_operator) #TODO
        expr = self.getArithmeticExpression()
        return #TODO


    def getPrintStatement(self):

    def getWhileStatement(self):
        tok = self.getNextToken()
        self.match(tok, tokentype.while_tok) #TODO
        expr = self.getBooleanExpression()
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, tokentype.end_tok)
    return #TODO



    def getForStatement(self):
        tok = self.getNextToken()
        self.match(tok, tokentype.for_tok) #TODO
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok,tokentype.colon_tok) #TODO
        expr = self.getBooleanExpression()
        self.match(tok,tokentype.end_tok) #TODO
        return #TODO


    def getIfStatement(self):

    def isValidStartOfStatement(self,tok):

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

    