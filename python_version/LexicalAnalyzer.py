from token import token
from tokentype import tokentype
import LexicalExcpetion

class LexicalAnalyzer():

    tokens = []

    def __init__(self, filename):
        if filename == "":
            raise TypeError("null file name argument")
        lineNumber = 0
        with open(filename) as f:
            for line in f:
                #print(line)
                lineNumber += 1
                self.processLine(line, lineNumber)
        f.close()
        new_tok = token(tokentype.EOS_TOK, "EOS", lineNumber, 1)
        self.tokens.append(new_tok)
        #print('[%s]' % ', '.join(map(str, self.tokens)))

    def processLine(self,line,lineNumber):
        #try:   
        if line == "":
            raise ValueError("null line argument")
        if lineNumber <= 0:
            raise ValueError("invalid line number argument")
        index = self.skipWhiteSpace(line, 0)

        while index < len(line):
            lexeme = self.getLexeme(line, index)
            tokType = self.getTokenType(lexeme, lineNumber, index + 1)
            #print(tokType) #TESTING CODE
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

            if lexeme[0].isdigit():
                if self.allDigits(lexeme):
                    tokType = tokentype.literal_integer #digit literal_integer | digit
                else:
                    print("literal integer expected " + " at row " + rowNumber + " and column " + columnNumber)
            elif lexeme[0].isalpha():

                if len(lexeme) == 1 and self.isValidIdentifier(lexeme[0]):
                    tokType = tokentype.id
                elif lexeme == "function":
                    tokType = tokentype.function_tok
                elif lexeme == "end":
                    tokType = tokentype.end_tok
                elif lexeme == "if":
                    tokType = tokentype.if_tok
                elif lexeme == "else":
                    tokType = tokentype.else_tok
                elif lexeme == "print":
                    tokType = tokentype.print_tok
                elif lexeme == "while":
                    tokType = tokentype.while_tok
                elif lexeme == "for":
                    tokType = tokentype.for_tok
                else:
                    print("Lexical Exception")

            elif self.isValidIdentifier(lexeme[0]):
                tokType = tokentype.id #letter
            elif lexeme == ">=":
                tokType = tokentype.ge_operator #>=
            elif lexeme == ">":
                tokType = tokentype.gt_operator #>
            elif lexeme == "<=":
                tokType = tokentype.le_operator #<=
            elif lexeme == "<":
                tokType = tokentype.lt_operator #<
            elif lexeme == "!=":
                tokType = tokentype.ne_operator  #<=
            elif lexeme == "==":
                tokType = tokentype.eq_operator  #= =
            elif lexeme == "%":
                tokType = tokentype.mod_operator  #%
            elif lexeme == "^":
                tokType = tokentype.exp_operator #^
            elif lexeme == "+":
                tokType = tokentype.add_operator #+
            elif lexeme == "-":
                tokType = tokentype.sub_operator #-
            elif lexeme == "*":
                tokType = tokentype.mul_operator #*
            elif lexeme == "/":
                tokType = tokentype.div_operator #// *
            #elif lexeme.equals("\""):
                #tokType = self.rev_div_operator         #\ * /
            elif lexeme == "=":
                tokType = tokentype.assignment_operator #=
            elif lexeme == "(":
                tokType = tokentype.left_parent
            elif lexeme == ")":
                tokType = tokentype.right_parent
            elif lexeme == ":":
                tokType = tokentype.colon_tok
            else:
                print ("Didn't set tokentype")
                raise LexicalExcpetion

            return tokType
        except LexicalExcpetion:
            print("invalid lexeme " + " at row " + rowNumber + " and column " + columnNumber)


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
            #print("HERE" + str(self.tokens[0]))
            return self.tokens.pop(0)
        except LexicalExcpetion:
            print("There aren't any more tokens")


    def isValidIdentifier(self, ch):
        if ch.isalpha() and ch.islower():
            return True
        else:
            return False
