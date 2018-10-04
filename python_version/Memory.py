class Memory:

    def __init__(self, mem):
        self.mem = range(53)
        
    def store(self, ch, value):
        self.mem[self.indexOf(ch)] = value;

    def indexOf(self, ch):

        if ch.isalpha() is not True:
            raise ValueError("invalid identifier argument")

        if ch == ch.upper():
            index = ch - 'a'
        else:
            index = 26 + ch - 'A'
        return index


    def fetch(self, ch):
        return self.mem[self.indexOf(ch)]



