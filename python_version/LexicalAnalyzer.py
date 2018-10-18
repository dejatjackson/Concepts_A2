from token import token
from tokentype import tokentype
import LexicalExcpetion

class LexicalAnalyzer():

    tokens = []

    def __init__(self, filename):
        if filename is None:
            raise TypeError("null file name argument")
        lineNumber = 0
        with open(filename) as f:
            for line in f:
                print(line)
                lineNumber += 1
                self.processLine(line, lineNumber)
        f.close()
        new_tok = token(tokentype.EOS_TOK, "EOS", lineNumber, 1)
        self.tokens.append(new_tok)


    def processLine(self,line,lineNumber):
        #try:
        if line is None:
            raise ValueError("null line argument")
        if lineNumber <= 0:
            raise ValueError("invalid line number argument")
        index = self.skipWhiteSpace(line, 0)

        while index < len(line):
            lexeme = self.getLexeme(line, index)
            tokType = self.getTokenType(lexeme, lineNumber, index + 1)
            print(tokType) #TESTING CODE
            n_tok = token(tokType, lexeme, lineNumber, index + 1)
            self.tokens.append(n_tok)
            #tokens.add(new token (tokType, lexeme, lineNumber, index + 1));
            index += len(lexeme)
            index = self.skipWhiteSpace(line, index)
        #except:
            #raise LexicalExcpetion


    def getTokenType(self,lexeme,rowNumber,columnNumber):
        try:
            if lexeme == None or len(lexeme) == 0:
                raise ValueError("invalid string argument")
            tokType = tokentype.EOS_TOK
            # if lexeme[0:3] == "fun":
            #     tokType = tokentype.function_tok
            # elif lexeme[0:3] == "pri":
            #     tokType = tokentype.print_tok
            if lexeme[0].isdigit():
                if self.allDigits(lexeme):
                    tokType = tokentype.literal_integer #digit literal_integer | digit
                else:
                  print("literal integer expected " + " at row " + rowNumber + " and column " + columnNumber)
            elif lexeme[0].isalpha():

                if len(lexeme) == 1 and self.isValidIdentifier(lexeme[0]):
                    tokType = tokentype.id
                elif lexeme is "function ":
                    tokType = tokentype.function_tok
                elif lexeme is "end":
                    tokType = tokentype.end_tok
                elif lexeme is "if":
                    tokType = tokentype.if_tok
                elif lexeme is "else":
                    tokType = tokentype.else_tok
                elif lexeme is "print":
                    tokType = tokentype.print_tok
                elif lexeme is "while":
                    tokType = tokentype.while_tok
                elif lexeme is "for":
                    tokType = tokentype.for_tok
                else:
                    print(tokType + " Lexical Exception")
            elif self.isValidIdentifier(lexeme[0]):
                tokType = tokentype.id #letter
            elif lexeme is ">=":
                tokType = tokentype.ge_operator #>=
            elif lexeme is ">":
                tokType = tokentype.gt_operator #>
            elif lexeme is "<=":
                tokType = tokentype.le_operator #<=
            elif lexeme is "<":
                tokType = tokentype.lt_operator #<
            elif lexeme is "!=":
                tokType = tokentype.ne_operator  #<=
            elif lexeme is"==":
                tokType = tokentype.eq_operator  #= =
            elif lexeme is "%":
                tokType = tokentype.mod_operator  #%
            elif lexeme is "^":
                tokType = tokentype.exp_operator #^
            elif lexeme is "+":
                tokType = tokentype.add_operator #+
            elif lexeme is "-":
                tokType = tokentype.sub_operator #-
            elif lexeme is "*":
                tokType = tokentype.mul_operator #*
            elif lexeme is "/":
                tokType = tokentype.div_operator #// *
            #elif lexeme.equals("\""):
                #tokType = self.rev_div_operator         #\ * /
            elif lexeme is "=":
                tokType = tokentype.assignment_operator #=
            elif lexeme is"(":
                tokType = tokentype.left_parent
            elif lexeme is ")":
                tokType = tokentype.right_parent
            elif lexeme is ":":
                tokType = tokentype.colon_tok
            else:
                print ("Didn't set tokentype")
                raise LexicalExcpetion

            return tokType
        except LexicalExcpetion:
            print( "invalid lexeme "+ " at row " + rowNumber  + " and column " + columnNumber)


    def allDigits(self, lexeme):
        if lexeme is None:
            raise TypeError("null string argument")
        i = 0
        while i < len(lexeme) and lexeme[i].isdigit():
            i += 1
        i = len(lexeme)
        return i

    def getLexeme(self,line, index):
        if line is None:
            raise ValueError("null string argument")
        if index < 0:
            raise ValueError("invalid index argument")
        i = index
        while i < len(line) and not line[i].isspace():
            i += 1
        return line[index:i]

    def skipWhiteSpace(self, line, index):
        while index < len(line) and line[index].isspace():
            index += 1
        return index


    def getLookaheadToken(self):
        try:
            if len(self.tokens) == 0:
                raise LexicalExcpetion
            return self.tokens[0]

        except LexicalExcpetion:
            print("No more tokens")

    def getNextToken(self):
        try:
            if len(self.tokens) == 0:
                raise LexicalExcpetion
            return self.tokens.remove(0)
        except LexicalExcpetion:
            print("There aren't any more tokens")



    def getForExpression(self):

        token = []
        for_tokens = token[3]

        for i in range (for_tokens.length - 1):
            for_tokens[i] = self.tokens[1]
        return for_tokens


    def isValidIdentifier(self, ch):
        if ch.isalpha() and ch.islower():
            return True
        else:
            return False
