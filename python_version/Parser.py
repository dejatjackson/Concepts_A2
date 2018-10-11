
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
            stmt = self.getStatement()
            blk.add(stmt)
            tok = self.getLookaheadToken()
        return blk

    def getStatement(self):
        #TODO how to i do the throws ParserException thing
        tok = self.getLookaheadToken()
        if tok.getTokType() == tokentype.if_tok:
            stmt = self.getIfStatement()
        elif tok.getTokType == tokentype.while_tok:
            stmt = self.getWhileStatement()
        elif tok.getTokType == tokentype.tokentype.print_tok:
                stmt = self.getPrintStatement()
        elif tok.getTokType == tokentype.tokentype.for_tok:
            stmt = self.getForStatement()
        elif tok.getTokType == tokentype.id:
            stmt = self.getAssignmentStatement()
        return stmt #TODO

    def getAssignmentStatement(self):
        var = self.getId()
        tok = self.getNextToken()
        self.match(tok, tokentype.assignment_operator)
        expr = self.getArithmeticExpression()
        return #TODO


    def getPrintStatement(self):
        tok = self.getNextToken()
        self.match(tok, tokentype)
        tok = self.getNextToken()
        self.match(tok, tokentype)
        expr = Arithmetic_expression.Arithmetic_expression()
        tok = self.getNextToken
        self.match(tok, tokentype) #TODO
        return PrintStatement.PrintStatement(expr)


    def getWhileStatement(self):
        tok = self.getNextToken()
        self.match(tok, tokentype.while_tok)
        expr = self.getBooleanExpression()
        blk = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, tokentype.end_tok)
        w_stmt = While_statement.While_statement(expr,blk)
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
        self.match(tok,tokentype.if_tok)
        expr = self.getBooleanExpression()
        blk1 = self.getBlock()
        tok = self.getNextToken()
        self.match(tok,tokentype.else_tok)
        blk2 = self.getBlock()
        tok = self.getNextToken()
        self.match(tok, tokentype.end_tok)
        f_stat = IfStatement.if_statement(expr, blk1, blk2)
        return f_stat

    def isValidStartOfStatement(self,tok):
        assert(tok != None)
        return tok.getTokType() == tokentype.id or  tok.getTokType() == tokentype.if_tok or tok.getTokType() == tokentype.while_tok or tok.getTokType() == tokentype.print_tok or tok.getTokType() == tokentype.for_tok


    def getArithmeticExpression(self):
        try:
            tok = self.getLookaheadToken
            if tok.getTokType() == tokentype.id: #TODO
                expr = self.getId()
            elif tok.getTokType() == tokentype.literal_integer: #TODO
                expr = self.getLiteralInteger()
            else:
                expr = self.getBinaryExpression()
            return expr
        except:
            raise ParserException



    def getBinaryExpression(self):
        op = self.getArithmeticOperator()
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        b_express = Binary_expression.Binary_expression(op,expr1,expr2)
        return b_express

    def getArithmeticOperator(self):
        op = Arithmetic_op.Arithmetic_op()
        tok = self.getNextToken()
        if tok.getTokType() == tokentype.add_operator():
            op = arithmetic #TODO

    def getLiteralInteger(self):
        try:
            tok = self.getNextToken()
            if tok.getTokType() != tokentype.literal_integer:
                raise ParserException("literal integer expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber()) #TODO
            value = Integer.parseInt(tok.getLexeme()) #TODO
            lit_int = Literal_Integer.Literal_integer(value)
            return lit_int
        except:
            raise ParserException

    def getId(self):
        try:
            tok = self.getNextToken()
            if tok.getTokType() != tokentype.id:
                #TODO exception
            return #TODO
        except:
            raise ParserException

    def getBooleanExpression(self):
        #TODO how to i do the throws ParserException thing
        try:
            op = self.getRelationalOperator()
            expr1 = self.getArithmeticExpression()
            expr2 = self.getArithmeticExpression()
            b_express = Boolean_expression.Boolean_expression(op,expr1,expr2)
            return b_express
        except:
            raise ParserException

    def getRelationalOperator(self):
        #TODO how to i do the throws ParserException thing

        op = None
        tok = self.getNextToken
        if tok.getTokType() == tokentype.eq_operator: #TODO
            op = Relative_op.eq_operator
        elif tok.getTokType() == tokentype.ne_operator: #TODO
            op = Relative_op.ne_operator
        elif tok.getTokType() == tokentype.gt_operator: #TODO
            op = Relative_op.gt_operator
        elif tok.getTokType() == tokentype.ge_operator: #TODO
            op = Relative_op.ge_operator
        elif tok.getTokType() == tokentype.lt_operator: #TODO
            op = Relative_op.lt_operator
        elif tok.getTokType() == tokentype.le_operator: #TODO
            op = Relative_op.le_operator
        else:
            raise ParserException ("relational operator expected at row " + tok.getRowNumber()  + " and column " + tok.getColumnNumber()) #TODO
        return op

    def match(self,tok, tokType):
        #TODO how to i do the throws ParserException thing

        assert(tok != None)
        assert(tokType != None)
        if tok.getTokType() != tokType:
            raise #TODO

    def getLookaheadToken(self):

        tok = None
        try:
            tok = lex.getLookaheadToken()
            raise ParserException
        except:
            print("no more tokens")
        return tok


    def getNextToken(self):

        tok = None
        try:
            tok = lex.getNextToken()
            raise ParserException
        except:
            print("no more tokens")
        return tok

    