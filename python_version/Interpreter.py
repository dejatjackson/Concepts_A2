import Parser
import ParserException
import Program
import LexicalExcpetion
import traceback

class Interpeter:
    pass

def main():
    try:
        parse = Parser.Parser("test4.jl")
        pro = Program.Program(parse)
        pro.execute()

    except ParserException:
        print("Parser Exception")
    except LexicalExcpetion:
        print("Lexical Exception")
    except ValueError:
        print("Illegal Argument")
    except Exception:
        print (traceback.print_exc() + "An exception has occurred")


if __name__ == '__main__':
    main()

