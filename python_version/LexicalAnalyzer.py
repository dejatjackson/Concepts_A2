import token
import tokentype
import LexicalExcpetion

class LexicalAnalyzer(token,tokentype,LexicalExcpetion):

    tokens = []

    def __init__(self, filename):
        if filename == None:
            raise TypeError("null file name argument")
        tokens = [] #TODO: Do I need this line - No
        input = raw_input(new File(filename))#TODO what is this in python
        lineNumber = 0
        while (input.hasNext()) #toDo has next in python - it doesn't exist
            line = input.nextLine() #TODO next line in python - doesn't exist

        #Is line even being used?



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
            raise LexicalExcpetion


    def getTokenType(self,lexeme,rowNumber,columnNumber):
        try:
            if lexeme == None or lexeme.length() == 0:
                raise ValueError("invalid string argument")
            tokType = self.EOS_TOK
            if lexeme.charAt(0).isdigit():
                if self.allDigits(lexeme):
                    tokType = self.literal_integer #digit literal_integer | digit
                else:
                  raise LexicalExcpetion("literal integer expected " + " at row " + rowNumber + " and column " + columnNumber)
            elif lexeme.charAt(0).isalpha():

                if lexeme.length() == 1 and self.isValidIdentifier(lexeme.charAt(0)):
                    tokType =self.id
                elif lexeme.equals("function"):
                    tokType = self.function_tok
                elif lexeme.equals("end"):
                    tokType = self.end_tok
                elif lexeme.equals("if"):
                    tokType = self.if_tok
                elif lexeme.equals("else"):
                    tokType = self.else_tok
                elif lexeme.equals("print"):
                    tokType = self.print_tok
                elif lexeme.equals("while"):
                    tokType = self.while_tok
                elif lexeme.equals("for"):
                    tokType = self.for_tok
                else:
                    raise LexicalExcpetion ( "invalid lexeme "+ " at row " + rowNumber  + " and column " + columnNumber)
            elif self.isValidIdentifier(lexeme.charAt(0)):
                tokType = self.id #letter
            elif lexeme.equals(">="):
                tokType = self.ge_operator #>=
            elif lexeme.equals(">"):
                tokType = self.gt_operator #>
            elif lexeme.equals("<="):
                tokType = self.le_operator #<=
            elif lexeme.equals("<"):
                tokType = self.lt_operator #<
            elif lexeme.equals("!="):
                tokType = self.ne_operator  #<=
            elif lexeme.equals("=="):
                tokType = self.eq_operator  #= =
            elif lexeme.equals("%"):
                tokType = self.mod_operator  #%
            elif lexeme.equals("^"):
                tokType = self.exp_operator #^
            elif lexeme.equals("+"):
                tokType = self.add_operator #+
            elif lexeme.equals("-"):
                tokType = self.sub_operator #-
            elif lexeme.equals("*"):
                tokType = self.mul_operator #*
            elif lexeme.equals("/"):
                tokType = self.div_operator #// *
            #elif lexeme.equals("\""):
                #tokType = self.rev_div_operator         #\ * /
            elif lexeme.equals ("="):
                tokType = self.assignment_operator #=
            elif lexeme.equals("("):
                tokType = self.left_parent
            elif lexeme.equals(")"):
                tokType = self.right_parent
            elif lexeme.equals(":"):
                tokType = self.colon_tok
            else:
                raise LexicalExcpetion ("invalid lexeme "+ " at row " + rowNumber  + " and column " + columnNumber)
            return tokType
        except:
            raise LexicalExcpetion


    def allDigits(self, lexeme):
        if lexeme == None:
            raise TypeError("null string argument")
        i = 0
        while i < lexeme.size() and lexeme.charAt(i).isdigit():
            i+= 1
        i  = lexeme.size()
        return i

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
                raise LexicalExcpetion("no more tokens")
            return self.tokens[0]

        except:
            raise LexicalExcpetion

    def getNextToken(self): #ToDO lexicalExpection part
        try:
            if len(self.tokens) == 0:
                raise LexicalExcpetion("There aren't any more tokens")
            return self.tokens.remove(0)
        except:
            raise LexicalExcpetion



    def getForExpression(self):

        for_tokens = token[3]

        for i in range (for_tokens.length - 1):
            for_tokens[i] = self.tokens[1]
        return for_tokens


    def isValidIdentifier(self, ch):
        if ch.isalpha() and ch.islower():
            return True
        else:
            return False
