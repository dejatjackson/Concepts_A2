from Parser import Parser
import ParserException
import Program
import LexicalExcpetion
import traceback

class Interpeter:
    pass

def main():
    try:
        parse = Parser("test1.jl")
        pro = parse.parse()
        pro.execute()
    except ParserException:
        print (traceback.print_exc())
        print("Parser Exception")
    except LexicalExcpetion:
        print (traceback.print_exc())
        print("Lexical Exception")
    except ValueError:
        print (traceback.print_exc())
        print("Illegal Argument")
    except Exception:
        print (traceback.print_exc())
        print("An error has occured")


if __name__ == '__main__':
    main()

