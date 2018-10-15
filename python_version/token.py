import tokentype

class token():
    def __init__(self, tokType, lexeme, rowNumber, colNumber):
        if tokType == None:
            raise TypeError("null TokenType argument")
        if lexeme == None or len(lexeme) == 0:
            raise TypeError("invalid lexeme argument")
        if rowNumber <= 0:
            raise TypeError("invalid row number argument")
        if colNumber <= 0:
            raise TypeError("invalid column number argument")
        self.tokType = tokType
        self.lexeme = lexeme
        self.rowNumber = rowNumber
        self.colNumber = colNumber

    def getTokType(self):
        return self.tokType
    def getLexeme(self):
        return self.lexeme

    def getRowNumber(self):
        return self.rowNumber

    def getColumnNumber(self):
        return self.colNumber

    def __str__(self):
        return "Line Number: " + self.getRowNumber() + " Lexeme Value: " + self.getLexeme() + " Token Type:" + self.getTokType()