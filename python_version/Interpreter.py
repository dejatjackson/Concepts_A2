from Parser import Parser
import ParserException
from Program import Program
import LexicalExcpetion


class Interpeter:

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
    if __name__ == '__main__':
        main()

