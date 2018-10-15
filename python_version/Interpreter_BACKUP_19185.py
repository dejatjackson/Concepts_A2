from Parser import Parser
import ParserException
from Program import Program
import LexicalExcpetion


class Interpeter:
    pass

def main():
    try:
        parse = Parser.Parser("test4.jl")
        pro = Program.Program(parse)
        pro.parse()     #TODO

    except ParserException:
        print("Parser Exception")
    except LexicalExcpetion:
        print("Lexical Exception")
    except ValueError:
        print("Illegal Argument")
    except Exception:
        print ("An exception has occurred")


<<<<<<< HEAD
    #TODO
    def main(self):
        try:
            parse = Parser("test1.jl")
            pro = Program.Program(parse)
            pro.parse()
        except ParserException:
            print("Parser Exception")
            #TODO: What's the right way to do this?
        except LexicalExcpetion:
            print("Lexical Exception")
        except ValueError:
            print("Illegal Argument")
        except Exception:
            print ("An exception has occurred")
=======
>>>>>>> 8a0a3b62ae88c277d7366c475bc9d1c12f4522fc
    if __name__ == '__main__':
        main()

