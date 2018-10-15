import Parser
import ParserException
import Program
import LexicalExcpetion


class Interpeter:

    #TODO
    def main(self):
        try:
            parse = Parser("test4.jl")
            pro = Program(parse)
            pro.parse()
        except ParserException:
            print('Parser Exception')
            #TODO: What's the right way to do this?
        except LexicalExcpetion:
            print('Lexical Exception')
        except IllegalArgumentException:
    if __name__ == '__main__':
        main()

