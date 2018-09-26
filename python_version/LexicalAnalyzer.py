import token
class LexicalAnalyzer():



    def __init__(self, filename):
        if filename == None
            raise TypeError("null file name argument")
        tokens = []
        input = raw_input(new File(filename))#what is this in python
        lineNumber = 0
        while (input.hasNext()) #toDo has next in python
            line = input.nextLine() #TODO next line in python

    
    def processLine

    def getTokenType

    def allDigits

    def getLexeme


    def skipWhiteSpace(self, line,index):
        while index < line.size() and Character.isWhiteSpace(line.charAt(index))
            index++
        return index


    def getLookaheadToken(self): #ToDO lexicalExpection part


    def getNextToken(self): #ToDO lexicalExpection part

    #ToDo: getForExpression

    def isValidIdentifer(self, ch):
        #TODO for the Character part
        if (Character.isLetter(ch) & & Character.isLowerCase(ch))
            return self.true
        else
            return self.false
