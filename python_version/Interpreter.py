from Parser import Parser
import ParserException
import Program
import LexicalExcpetion
import traceback

class Interpeter:
    pass

def main():
    try:
        pars = Parser("test3.jl")
        pro = pars.parse()
        pro.execute()
    except ParserException as e:
        print (traceback.print_exc())
        print(e.message)
    except LexicalExcpetion as e:
        print (traceback.print_exc())
        print(e.message)
    except ValueError as e:
        print (traceback.print_exc())
        print (e.message)
    except Exception as e:
        print (traceback.print_exc())
        print (e.message)


if __name__ == '__main__':
    main()

