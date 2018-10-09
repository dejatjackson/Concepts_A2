
#TODO - complete all methods below
import ParserException
import While_statement
import token
import PrintStatement
from tokentype import tokentype
import Block
import Literal_Integer
import Statement
import Boolean_expression
import Arithmetic_expression
import IfStatement
import ForStatement
import Binary_expression
import Arithmetic_op
from Relative_op import Relative_op



class Parser():

    global lex

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
        elif tok.getTokType == tokentype.while_tok: #TODO
            stmt = self.getWhileStatement()
        elif tok.getTokType == tokentype.tokentype.print_tok:  #TODO
                stmt = self.getPrintStatement()
        elif tok.getTokType == tokentype.tokentype.for_tok: #TODO
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
        tok = self.getNextToken()
        self.match(tok, tokentype) #TODO
        tok = self.getNextToken()
        self.match(tok, tokentype) #TODO
        expr = Arithmetic_expression.Arithmetic_expression()
        tok = self.getNextToken
        self.match(tok, tokentype) #TODO
        return PrintStatement.PrintStatement(expr)


    def getWhileStatement(self):
        tok = self.getNextToken()
        self.match(tok, tokentype.while_tok) #TODO
        expr = self.getBooleanExpression()
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, tokentype.end_tok)
        w_stmt = While_statement(expr,blk)
        return w_stmt



    def getForStatement(self):
        tok = self.getNextToken()
        self.match(tok, tokentype.for_tok)
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok,tokentype.colon_tok)
        expr = self.getBooleanExpression()
        self.match(tok,tokentype.end_tok)
        f_stat = ForStatement.ForStatement(expr,blk)
        return f_stat


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
        op = Arithmetic_op.Arithmetic_op()
        tok = self.getNextToken()
        if tok.getTokType() == tokentype.add_operator():
            op = arithmetic

    def getLiteralInteger(self):
      # TODO how to i do the throws ParserException thing
        tok = getNextToken();
        if tok.getTokType() != tokentype.literal_integer:
            raise ParserException("literal integer expected at row " +
                    tok.getRowNumber() + " and column " + tok.getColumnNumber())
        value = Integer.parseInt(tok.getLexeme())
        lit_int = Literal_integer.Literal_integer(value)
        return lit_int

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
        #TODO how to i do the throws ParserException thing

        op = None
        tok = self.getNextToken
        if tok.getTokType() == tokentype.eq_operator
            op = Relative_op.eq_operator
        elif tok.getTokType() == tokentype.ne_operator:
            op = Relative_op.ne_operator #TODO
        elif tok.getTokType() == tokentype.gt_operator:
            op = Relative_op.gt_operator
        elif tok.getTokType() == tokentype.ge_operator:
            op = Relative_op.ge_operator
        elif tok.getTokType() == tokentype.lt_operator:
            op = Relative_op.lt_operator
        elif tok.getTokType() == tokentype.le_operator:
            op = Relative_op.le_operator
        else
            raise ParserException ("relational operator expected at row " +
            tok.getRowNumber()  + " and column " + tok.getColumnNumber()) #TTODO
        return op

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

    