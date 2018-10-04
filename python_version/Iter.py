class Iter:

    def getCurrent(self, index, tokens):

        if self.tokens[0] is None:
            raise ValueError("List cannot be empty!")

        else:
            return tokens[index];

    def getLast(self, index, tokens):
        if tokens[0] is None:
            raise ValueError("List cannot be empty!")

        index -= 1

        if tokens[index] is None:
            raise ValueError("Index does not exist!")

        else:
            return tokens[index]

    def getNext(self, index, tokens):
        index += 1

        if tokens[index] is None:
            raise ValueError("Index does not exist!")

        return tokens[index]

