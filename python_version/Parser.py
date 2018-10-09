
#TODO - complete all methods below
import ParserException
import token
import Block
import Statement
import Boolean_expression
import Arthmetic_expression
import IfStatement
import Binary_expression


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
        tok = self.getNextToken()
        self.match(tok,tokentype.if_tok) #TODO
        expr = self.getBooleanExpression()
        blk1 = self.getBlock()
        tok = self.getNextToken()
        self.match(tok,tokentype.else_tok) #TODO
        blk2 = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, tokentype.end_tok) #TODO
        f_stat = IfStatement.if_statement(expr, blk1, blk2)
        return f_stat

    def isValidStartOfStatement(self,tok):
        assert(tok != None)
        return tok.getTokType() == tokentype.id || tok.getTokType() == tokentype.if_tok ||
                tok.getTokType() == tokentype.while_tok || tok.getTokType() == tokentype.print_tok }}
                tok.getTokType() == tokentype.for_tok #TODO


    def getArithmeticExpression(self):
        #TODO how to i do the throws ParserException thing
        tok = self.getLookaheadToken
        if tok.getTokType() == tokentype.id: #TODO
            expr = self.getID()
        elif tok.getTokType() == tokentype.literal_integer: #TODO
            expr = self.getLiteralInteger()
        else:
            expr = self.getBinaryExpression()
        return expr


    def getBinaryExpression(self):
        op = self.getArithmeticOperaor()
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        b_express = Binary_expression.Binary_expression(op,expr1,expr2)
        return b_express

    def getArithmeticOperator(self):
        #TODO CODE

    def getLiteralInteger(self):
      # TODO how to i do the throws ParserException thing


def getId(self):
        #TODO how to i do the throws ParserException thing

        tok = self.getNextToken()
        if tok.getTokType() != tokentype.id: #TODO
            #TODO exception
        return #TODO

    def getBooleanExpression(self):
        #TODO how to i do the throws ParserException thing
        op = self.getRelationalOperator()
        expr1 = self.getArthimeticExpression()
        expr2 = self.getArthimeticExpression()
        b_express = Boolean_expression.Boolean_expression(op,expr1,expr2)
        return b_express

    def getRelationalOperator(self):
        tok = self.getNextToken

       #TODO

    def match(self,tok, tokType):
        #TODO how to i do the throws ParserException thing

        assert(tok != None)
        assert(tokType != None)
        if tok.getTokType() != tokType:
            raise #TODO

    def getLookaheadToken(self): #TODO - I think this is wrong, just saying
        #TODO how to i do the throws ParserException thing

        tok = None
        try:
            tok = lex.getLookaheadToken()
            raise ParserException
        except:
            print("no more tokens")
        return tok


    def getNextToken(self): #TODO - I think this is wrong, just saying
        # TODO how to i do the throws ParserException thing

        tok = None
            try:
                tok = lex.getNextToken()
                raise ParserException
            except:
                print("no more tokens")
            return tok

    