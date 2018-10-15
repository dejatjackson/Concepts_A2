
#TODO - complete all methods below
import ParserException
import Assignment_statement
import While_statement
import token
import PrintStatement
from tokentype import tokentype
import Block
import Literal_Integer
import Statement
import Program
import Boolean_expression
import Arithmetic_expression
import IfStatement
import ForStatement
import Binary_expression
import ID
from Arithmetic_op import Arithmetic_op
from Relative_op import Relative_op



class Parser():

    global lex

    def _init_(self, filename):
        self.filename = filename

    def parse(self):
        try:
            tok = self.getNextToken()
            self.match(tok, tokentype.function_tok)
            functionName = self.getId()
            tok = self.getNextToken()
            self.match(tok, tokentype.id.left_parent)
            tok = self.getNextToken()
            self.match(tok, tokentype.right_parent)
            blk = self.getBlock()
            tok = self.getNextToken()
            self.match(tok, tokentype.end_tok)
            tok = self.getNextToken()
            if tok.getTokType() != tokentype.EOS_TOK:
                raise ParserException
            return Program.Program(blk)
        except ParserException:
            print("garbage at the end of the file")

    def getBlock(self):

        try:
            blk = Block.Block()
            tok = self.getLookaheadToken()
            while(self.isValidStartOfStatement(tok)):
                stmt = self.getStatement()
                blk.add(stmt)
                tok = self.getLookaheadToken()
            return blk
        except:
            raise ParserException

    def getStatement(self):

        tok = self.getLookaheadToken()
        try:
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
            else:
                raise ParserException
            return stmt
        except ParserException:
            print("invalid statement at row " + tok.getRowNumber()  + " and column " + tok.getColumnNumber())

    def getAssignmentStatement(self):
        try:
            var = self.getId()
            tok = self.getNextToken()
            self.match(tok, tokentype.assignment_operator)
            expr = self.getArithmeticExpression()
            return Assignment_statement.Assignment_statement(var,expr)
        except:
            raise ParserException

    def getPrintStatement(self):
        try:
            tok = self.getNextToken()
            self.match(tok, tokentype.print_tok)
            tok = self.getNextToken()
            self.match(tok, tokentype.left_parent)
            expr = Arithmetic_expression.Arithmetic_expression()
            tok = self.getNextToken()
            self.match(tok, tokentype.right_parent)
            return PrintStatement.PrintStatement(expr)
        except:
            raise ParserException

    def getWhileStatement(self):
        try:
            tok = self.getNextToken()
            self.match(tok, tokentype.while_tok)
            expr = self.getBooleanExpression()
            blk = self.getBlock()
            tok = self.getNextToken()
            self.match(tok, tokentype.end_tok)
            w_stmt = While_statement.While_statement(expr,blk)
            return w_stmt
        except:
            raise ParserException


    def getForStatement(self):
        try:
            tok = self.getNextToken()
            self.match(tok, tokentype.for_tok)
            blk = self.getBlock()
            tok = self.getNextToken()
            self.match(tok,tokentype.colon_tok)
            expr = self.getBooleanExpression()
            self.match(tok,tokentype.end_tok)
            f_stat = ForStatement.ForStatement(expr,blk)
            return f_stat
        except:
            raise ParserException


    def getIfStatement(self):
        try:
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
        except:
            raise ParserException

    def isValidStartOfStatement(self,tok):
        assert(tok != None)
        return tok.getTokType() == tokentype.id or tok.getTokType() == tokentype.if_tok or tok.getTokType() == tokentype.while_tok or tok.getTokType() == tokentype.print_tok or tok.getTokType() == tokentype.for_tok


    def getArithmeticExpression(self):
        try:
            tok = self.getLookaheadToken()
            if tok.getTokType() == tokentype.id:
                expr = self.getId()
            elif tok.getTokType() == tokentype.literal_integer:
                expr = self.getLiteralInteger()
            else:
                expr = self.getBinaryExpression()
            return expr
        except:
            raise ParserException



    def getBinaryExpression(self):
        try:
            op = self.getArithmeticOperator()
            expr1 = self.getArithmeticExpression()
            expr2 = self.getArithmeticExpression()
            b_express = Binary_expression.Binary_expression(op,expr1,expr2)
            return b_express
        except:
            raise ParserException

    def getArithmeticOperator(self):
        op = Arithmetic_op.Arithmetic_op()
        tok = self.getNextToken()
        try:

            if tok.getTokType() == tokentype.add_operator:
                op = Arithmetic_op.add_operator
            elif tok.getTokType() == tokentype.sub_operator:
                op = Arithmetic_op.sub_operator
            elif tok.getTokType() == tokentype.mul_operator:
                op = Arithmetic_op.mul_operator
            elif tok.getTokType() == tokentype.div_operator:
                op = Arithmetic_op.div_operator
            else:
                raise ParserException
            return op
        except ParserException:
            print("arithmetic operator expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())



    def getLiteralInteger(self):
        tok = self.getNextToken()
        try:
            if tok.getTokType() != tokentype.literal_integer:
                raise ParserException
            value = int(tok.getLexeme())
            lit_int = Literal_Integer.Literal_integer(value)
            return lit_int
        except ParserException:
            print("literal integer expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())

    def getId(self):
        tok = self.getNextToken()

        try:
            if tok.getTokType() != tokentype.id:
                raise ParserException
            return ID.ID(tok.getLexeme().charAt(0))
        except ParserException:
            print("identifier expected at row " + tok.getRowNumber()  + " and column " + tok.getColumnNumber())

    def getBooleanExpression(self):
        try:
            op = self.getRelationalOperator()
            expr1 = self.getArithmeticExpression()
            expr2 = self.getArithmeticExpression()
            b_express = Boolean_expression.Boolean_expression(op,expr1,expr2)
            return b_express
        except:
            raise ParserException

    def getRelationalOperator(self):
        op = None
        tok = self.getNextToken()
        try:

            if tok.getTokType() == tokentype.eq_operator:
                op = Relative_op.eq_operator
            elif tok.getTokType() == tokentype.ne_operator:
                op = Relative_op.ne_operator
            elif tok.getTokType() == tokentype.gt_operator:
                op = Relative_op.gt_operator
            elif tok.getTokType() == tokentype.ge_operator:
                op = Relative_op.ge_operator
            elif tok.getTokType() == tokentype.lt_operator:
                op = Relative_op.lt_operator
            elif tok.getTokType() == tokentype.le_operator:
                op = Relative_op.le_operator
            else:
                raise ParserException#
            return op
        except ParserException:
            print("relational operator expected at row " + tok.getRowNumber()  + " and column " + tok.getColumnNumber())

    def match(self,tok, tokType):
        try:

            assert(tok != None)
            assert(tokType != None)
            if tok.getTokType() != tokType:
                raise ParserException
        except:
            print(tokType + " expected at row " + tok.getRowNumber()  + " and column " + tok.getColumnNumber())

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

    