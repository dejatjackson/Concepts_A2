import token
import tokentype
import LexicalException

class LexicalAnalyzer():

    tokens = []

    def __init__(self, filename):
        if filename == None:
            raise TypeError("null file name argument")
        tokens = [] #TODO: Do I need this line
        input = raw_input(new File(filename))#what is this in python
        lineNumber = 0
        while (input.hasNext()) #toDo has next in python
            line = input.nextLine() #TODO next line in python


    def processLine(self,line,lineNumber):
        try:
            if line == None:
                raise ValueError("null line argument")
            if lineNumber <= 0:
                raise ValueError("invalid line number argument")
            index = self.skipWhiteSpace(line, 0)

            while index < line.length():
                lexeme = self.getLexeme(line, index)
                tokType = self.getTokenType(lexeme, lineNumber, index + 1)
                self.tokens.append(token(tokType, lexeme, lineNumber, index + 1)) #TODO
                index += lexeme.length()
                index = self.skipWhiteSpace(line, index)
        except:
            raise LexicalException


    def getTokenType(self,lexeme,rowNumber,columnNumber):
        try:
            if lexeme == None or lexeme.length() == 0:
                raise ValueError("invalid string argument")
            tokType = tokentype.EOS_TOK
            if lexeme.charAt(0).isdigit():
                if self.allDigits(lexeme):
                    tokType = tokentype.literal_integer #literal_integer → digit literal_integer | digit
                else:
                  raise LexicalException("literal integer expected " + " at row " + rowNumber + " and column " + columnNumber)
            elif lexeme.charAt(0).isalpha():

                if lexeme.length() == 1 and self.isValidIdentifer(lexeme.charAt(0)):
                    tokType = tokentype.id
                elif lexeme.equals("function"):
                    tokType = tokentype.function_tok
                elif lexeme.equals("end"):
                    tokType = tokentype.end_tok
                elif lexeme.equals("if"):
                    tokType = tokentype.if_tok
                elif lexeme.equals("else"):
                    tokType = tokentype.else_tok
                elif lexeme.equals("print"):
                    tokType = tokentype.print_tok
                elif lexeme.equals("while"):
                    tokType = tokentype.while_tok
                elif lexeme.equals("for"):
                    tokType = tokentype.for_tok
                else:
                    raise LexicalException ( "invalid lexeme "+ " at row " + rowNumber  + " and column " + columnNumber)
            elif isValidIdentifier(lexeme.charAt(0)):
                tokType = tokentype.id; #id → letter
            elif lexeme.equals(">="):
                tokType = tokentype.ge_operator #ge_operator → >=
            elif lexeme.equals(">"):
                tokType = tokentype.gt_operator # gt_operator → >
            elif lexeme.equals("<="):
                tokType = tokentype.le_operator #le_operator → <=
            elif lexeme.equals("<"):
                tokType = tokentype.lt_operator #lt_operator → <
            elif lexeme.equals("!="):
                tokType = tokentype.ne_operator  #ne_operator → <=
            elif lexeme.equals("=="):
                tokType = tokentype.eq_operator  #eq_operator → = =
            elif lexeme.equals("%"):
                tokType = tokentype.mod_operator  #mod_operator → = =
            elif lexeme.equals("^"):
                tokType = tokentype.exp_operator #exp_operator → ^
            elif lexeme.equals("+"):
                tokType = tokentype.add_operator #add_operator → +
            elif lexeme.equals("-"):
                tokType = tokentype.sub_operator #sub_operator → -
            elif lexeme.equals("*"):
                tokType = tokentype.mul_operator #mul_operator → *
            elif lexeme.equals("/"):
                tokType = tokentype.div_operator #div_operator → // *
            #elif lexeme.equals("\""):
                #tokType = tokentype.rev_div_operator         #rev_div_operator → \ * /
            elif lexeme.equals ("="):
                tokType = tokentype.assignment_operator #assignment_operator → =
            elif lexeme.equals("("):
                tokType = tokentype.left_parent
            elif lexeme.equals(")"):
                tokType = tokentype.right_parent
            elif lexeme.equals(":"):
                tokType = tokentype.colon_tok
            else:
                raise LexicalException ("invalid lexeme "+ " at row " + rowNumber  + " and column " + columnNumber)
            return tokType
        except:
            raise LexicalException


    def allDigits(self, lexeme):
        if lexeme == None:
            raise TypeError("null string argument")
        i = 0
        while i < lexeme.size() and lexeme.charAt(i).isdigit():
            i+= 1
        return i = lexeme.size() #TODO

    def getLexeme(self,line, index):
        if line == None:
            raise ValueError("null string argument")
        if index < 0:
            raise ValueError("invalid index argument")
        i = index
        while i < line.length() and not line.charAt(i).isspace():
            i += 1
        return line.substring(index, i)

    def skipWhiteSpace(self, line, index):
        while index < line.length() and line.charAt(index).isspace():
            index += 1
        return index


    def getLookaheadToken(self):
        try:
            if len(self.tokens) == 0:
                raise LexicalException("no more tokens")
            return self.tokens[0]

        except:
            raise LexicalException

    def getNextToken(self): #ToDO lexicalExpection part
        try:
            if len(self.tokens) == 0:
                raise LexicalException("There aren't any more tokens")
            return self.tokens.remove(0)
        except:
            raise LexicalException



    def getForExpression(self):

        for_tokens = token[3]

        for i in range (for_tokens.length - 1):
            for_tokens[i] = self.tokens[1]
        return for_tokens


    def isValidIdentifer(self, ch):
        if ch.isalpha() and ch.islower():
            return True
        else:
            return False
